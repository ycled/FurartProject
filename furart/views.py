# Create your views here.

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from furart.forms import MessageForm, ActivityForm
from furart.models import Message, Activity


def index(request):
    if request.method == "GET":           # no user name provided
        return render(request, 'furart/index.html')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            user = User(username = username,
                        password = password,
                        email = email)
            user.save()
            return HttpResponseRedirect('/furart/activity_post_success/')

    return render_to_response('furart/index.html',
                              {'username': username},
                              context_instance=RequestContext(request))


def signup(request):
    return render(request, 'furart/signup.html');

def signin(request):
    return render(request, 'furart/signup.html');

def activity(request):
    return render(request, 'furart/activity.html');

# post a new activity    
def activity_post(request): 
    if request.method == 'POST': 
        form = ActivityForm(request.POST) 
        if form.is_valid(): 
            title = form.cleaned_data['title'] 
            activitytype = form.cleaned_data['activitytype'] 
            organizor = form.cleaned_data['organizor'] 
            location = form.cleaned_data['location'] 
            detail = form.cleaned_data['detail']


            m = Activity(title = title,
                        activitytype = activitytype,
                        organizor= organizor,
                        location = location,
                        detail = detail,
                        ) 
            m.save() 
            #return HttpResponseRedirect('furart/message/') 
            return HttpResponseRedirect('/furart/activity_post_success/') 
    else: 
        form = ActivityForm()
        
    activitys = Activity.objects.all().order_by('-time') 
    
    return render_to_response('furart/activity_post.html', 
                              {'form': form, 'activitys': activitys},
                              context_instance=RequestContext(request))
    


# post new acitivity successfully
def activity_post_success(request):
    return render(request, 'furart/activity_post_success.html');



# # search activity
# def activity_search(request):
#     errors = []
#     form = ActivitySearchForm(request.GET)
#     if 'location' in request.GET:
#         location = request.GET['location']
#         if not location:
#             errors.append('Enter a location')
#             
#         else:
#             activitys = Activity.objects.filter(title__icontains=location)
#             return render_to_response('furart/activity_search.html', 
#                 {'form': form, 'activitys': activitys},context_instance=RequestContext(request))
#             
# #     return render_to_response('activity_search.html',
# #         {'errors': errors})
# 
#             return render_to_response('activity_search.html')



# search activity by location
def activity_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        activitys = Activity.objects.filter(title__icontains=q)
        return render_to_response('furart/activity_search_result.html',
                                  {'activitys': activitys, 'query': q})
    else:
        return render_to_response('furart/activity_search.html', {'error': True})


# post new acitivity successfully
def activity_search_result(request):
    return render(request, 'furart/activity_search_result.html');





    
    

#sample!!TODO: to be removed!
def message(request): 
    if request.method == 'POST': 
        form = MessageForm(request.POST) 
        if form.is_valid(): 
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            homepage = form.cleaned_data['homepage'] 
            title = form.cleaned_data['title'] 
            content = form.cleaned_data['content'] 
            ip = request.META['REMOTE_ADDR'] 
            m = Message(name=name, 
                        email=email, 
                        homepage=homepage, 
                        title=title, 
                        content=content, 
                        ip=ip) 
            m.save() 
            #return HttpResponseRedirect('furart/message/') 
            return HttpResponseRedirect('furart/activity_post_success') 
    else: 
        form = MessageForm() 
    messages = Message.objects.all().order_by('-time') 
    return render_to_response('furart/message.html', 
                {'form': form, 'messages': messages},context_instance=RequestContext(request))
