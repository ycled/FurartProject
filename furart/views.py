from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from furart.forms import UserForm
from furart.forms import ActivityForm

from furart.models import Activity
from furart.models import User




# search by type
# nav bar
# all type
def event_search_all(request):

    try:
        activitys = Activity.objects.filter()       
    except Activity.DoesNotExist:
        activitys = None
        ###TODO
        print "no activity found"
        
        return render_to_response('furart/event_search.html',
            {'activitys': activitys})
    else:
        return render_to_response('furart/event_search.html', {'error': True})



# search by type
# nav bar
def event_search(request, type):
    ###TODO
    print "activity_type = " + type
    
    try:
        if type == 'all' or type == '':
            print "all"
            activitys = Activity.objects.all()
        else:
            print "type!!!"
            activitys = Activity.objects.filter(activitytype__icontains=type)       
    except Activity.DoesNotExist:
        print "no activity found"
        activitys = None
        
        
    return render_to_response('furart/event_search.html',{'activitys': activitys})

    
    
    

# edit a exited activity
def activity_edit(request, activity_id): 
    ###TODO:
    print "activity_edit: " + activity_id 
    
    try:
        activity = Activity.objects.get(pk=activity_id)        
    except Activity.DoesNotExist:
        activity = None
        print "activity not found"
    
    if request.method == 'POST': 
        #form = ActivityForm(request.POST, request.FILES, activity=activity)              
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
                                     'time': activity.time,})
        
                   
    return render_to_response('furart/edit.html',
                              {'form': form, 'activity': activity},
                              context_instance=RequestContext(request))


# edit activity successfully
def activity_edit_success(request):
    return render(request, 'furart/activity_edit_success.html');



# display activity detail
def activity_detail(request, activity_id):
    
    ###TODO:
    print "activity_detail: " + activity_id 
    
    
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        raise Http404
    return render(request, 'furart/activity_detail.html', {'activity': activity})



# post a new activity
def activity_post(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            activitytype = form.cleaned_data['activitytype']
            organizor = form.cleaned_data['organizor']
            location = form.cleaned_data['location']
            detail = form.cleaned_data['detail']
            
            ###
            time = form.cleaned_data['time']
            
            
            m = Activity(title=title,
                        activitytype=activitytype,
                        organizor=organizor,
                        location=location,
                        detail=detail,
                        # picture = null
                        time = time,
                        ) 
            m.save() 
            # return HttpResponseRedirect('furart/message/') 
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
    if request.session.get('username', False):   # if the user has already logged in
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

            user = User(username = username,
                        password = password,
                        email = email)
            user.save()
            request.session['username'] = username
            return HttpResponseRedirect('/furart/')
    else: # if the request is GET, output a new form
        form = UserForm()

    return render_to_response('furart/signup.html',
                              {'form': form},
                              context_instance=RequestContext(request))
