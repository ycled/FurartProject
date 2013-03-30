from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from furart.forms import ActivityForm, UserForm
from furart.models import Activity, User
import datetime
from datetime import timedelta


################################
#    
#    Event
#
#################################


# post a new event
def activity_post(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            
            uploader = request.session.get('username')
            title = form.cleaned_data['title']
            activitytype = form.cleaned_data['activitytype']
            organizer = form.cleaned_data['organizer']
            location = form.cleaned_data['location']
            detail = form.cleaned_data['detail']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            
            m = Activity(uploader=uploader,
                         title=title,
                         activitytype=activitytype,
                         organizer=organizer,
                         location=location,
                         detail=detail,
                         poster=request.FILES['poster'],
                         start_date = start_date,
                         start_time = start_time,
                         end_date = end_date,
                         end_time = end_time,
                         )
            m.save() 
            return HttpResponseRedirect('/furart/activity_post_success/') 
    else: 
        form = ActivityForm()
        
    activitys = Activity.objects.all().order_by('-time') 
            
    return render_to_response('furart/activity_post.html',
                              {'form': form, 'activitys': activitys},
                              context_instance=RequestContext(request))



# post new activity successfully
def activity_post_success(request):
    return render(request, 'furart/activity_post_success.html');




# display activity detail
def activity_detail(request, activity_id):
    
    # ##TODO:
    print "activity_detail: " + activity_id 
    
    
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        raise Http404
    return render(request, 'furart/activity_detail.html', {'activity': activity})



# search by type
# nav bar
def event_search(request, activity_type, activity_time):
    
    
    if activity_type == None:
        activity_type = ''
    if activity_time == None:
        activity_time = ''
    
    # ##TODO
    print "activity_type = " + activity_type 
    print "activity_time = " + activity_time
    
    
    if activity_time == "today":
        deltaday = 0
    elif activity_time == "tomorrow":
        deltaday = 1
    # ##TODO: week and month not correct    
    elif activity_time == "week":
        deltaday = 7
    elif activity_time == "month":
        deltaday = 30
    else:
        deltaday = 0
    
    # ##
    print "AAA today= %r" % datetime.date.today()
    print "AAA weekday= %d" % datetime.date.today().weekday()
        
    try:
        if activity_type == '' and activity_time == '':
            activitys = Activity.objects.all()
                
        else:
            today = datetime.date.today()
            
            if activity_time == "today":
                activitys = Activity.objects.filter(activitytype__icontains=activity_type, time__iexact=datetime.date.today())
            elif activity_time == "tomorrow":
                activitys = Activity.objects.filter(activitytype__icontains=activity_type, time__iexact=datetime.date.today() + timedelta(days=1))   
            elif activity_time == "week":
                end_week = today - timedelta(today.weekday()) + timedelta(7)
                print "AAA end_week= %r" % end_week
                activitys = Activity.objects.filter(activitytype__icontains=activity_type, time__range=[today, end_week])
            elif activity_time == "month":
                activitys = Activity.objects.filter(activitytype__icontains=activity_type, time__month=today.month)
            else:
                activitys = Activity.objects.filter(activitytype__icontains=activity_type)
                   
    except Activity.DoesNotExist:
        print "no activity found"
        activitys = None
        
        
    return render_to_response('furart/event_search.html', {'activitys': activitys, 'activity_type': activity_type})



# edit a exited activity
def activity_edit(request, activity_id): 
    # ##TODO:
    print "activity_edit: " + activity_id 
    
    try:
        activity = Activity.objects.get(pk=activity_id)        
    except Activity.DoesNotExist:
        activity = None
        print "activity not found"
    
    if request.method == 'POST': 
        # form = ActivityForm(request.POST, request.FILES, activity=activity)     
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid(): 
            title = form.cleaned_data['title'] 
            activitytype = form.cleaned_data['activitytype'] 
            organizor = form.cleaned_data['organizor'] 
            location = form.cleaned_data['location'] 
            detail = form.cleaned_data['detail']
            
          
            activity.title = title

            activity.save()
            return HttpResponseRedirect('/furart/activity_edit_success/') 
    else: 
        form = ActivityForm(initial={'title': activity.title,
                                     'time': activity.time, })
        
                   
    return render_to_response('furart/edit.html',
                              {'form': form, 'activity': activity},
                              context_instance=RequestContext(request))


# edit activity successfully
def activity_edit_success(request):
    return render(request, 'furart/activity_edit_success.html');







# search by text input
# search activity by location
def activity_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        activitys = Activity.objects.filter(title__icontains=q)
        return render_to_response('furart/activity_search_result.html',
                                  {'activitys': activitys, 'query': q})
    else:
        return render_to_response('furart/activity_search.html', {'error': True})



# post new activity successfully
def activity_search_result(request):
    return render(request, 'furart/activity_search_result.html');






# # search by select form
# # search event by type
# def event_search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         activitys = Activity.objects.filter(activitytype__icontains=q)
#         return render_to_response('furart/event_search.html',
#             {'activitys': activitys, 'query': q})
#     else:
#         return render_to_response('furart/event_search.html', {'error': True})



def activity(request):
    return render(request, 'furart/activity.html');



#-------------------------------------------------------------
# user management
#-------------------------------------------------------------
def index(request):
    if request.session.get('username', False):  # if the user has already logged in
        username = request.session['username']
        return render_to_response('furart/index.html',
                                  {"username": username},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('furart/index.html')


def signin(request):
    return render(request, 'furart/signup.html');


def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/furart/')


def signup(request):
    if request.method == 'POST':  # signup a new user
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            user = User(username=username,
                        password=password,
                        email=email)
            user.save()
            request.session['username'] = username
            return HttpResponseRedirect('/furart/')
    else:  # if the request is GET, output a new form
        form = UserForm()

    return render_to_response('furart/signup.html',
                              {'form': form},
                              context_instance=RequestContext(request))
