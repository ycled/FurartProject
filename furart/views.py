# Create your views here.

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from furart.forms import ActivityForm, UploadFileForm
from furart.models import Activity

def index(request):
    return render(request, 'furart/index.html')

def signup(request):
    return render(request, 'furart/signup.html');


def activity(request):
    return render(request, 'furart/activity.html');










#  create new event
def event_create(request): 
    errors = []
    if request.method == 'POST': 
        # error check
        if not request.POST.get('type', ''):
            errors.append('type')
        if not request.POST.get('title', ''):
            errors.append('title')
            
        if not errors:
            m = Activity(title = request.POST['title'],
                        activitytype = request.POST['activitytype'],
                        organizor= request.POST['organizor'],
                        location = request.POST['location'],
                        detail = request.POST['detail'],
                        ) 
            m.save() 
            #return HttpResponseRedirect('furart/message/') 
            return HttpResponseRedirect('/furart/event_create_success/') 
        else:
            return render_to_response('/furart/event_create/',{'errors': errors})
        
    activitys = Activity.objects.all().order_by('-time')   
    return render_to_response('furart/event_create.html', 
                {'activitys': activitys},context_instance=RequestContext(request))
    
    


# post new acitivity successfully
def event_create_success(request):
    return render(request, 'furart/activity_post_success.html');









    
    
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
                {'form': form, 'activitys': activitys},context_instance=RequestContext(request))
    
    


# post new acitivity successfully
def activity_post_success(request):
    return render(request, 'furart/activity_post_success.html');













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












#form in html
# search event by type
def event_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        activitys = Activity.objects.filter(activitytype__icontains=q)
        return render_to_response('furart/event_search.html',
            {'activitys': activitys, 'query': q})
    else:
        return render_to_response('furart/event_search.html', {'error': True})


# # form
# # search event by type
# def event_search(request):
#     
#     if 'activitytype' in request.GET and request.GET['activitytype']:
#         form = ActivitySearchForm(request.GET) 
# 
#         if form.is_valid(): 
#             activitytype = form.cleaned_data['activitytype'] 
# 
# 
#         #activitytype = request.GET['activitytype']
#         print activitytype
#         activitys = Activity.objects.filter(activitytype__icontains=activitytype)
#         return render_to_response('furart/event_search.html',
#             {'form': form, 'activitys': activitys, 'query': activitytype})
#     else:
#         form = ActivitySearchForm() 
#         return render_to_response('furart/event_search.html', {'form': form, 'error': True})





def upload_image(request):
    '''Simple view method for uploading an image
 
    '''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            save_file(request.FILES['image'])
            return HttpResponse('Thanks for uploading the image')
        else:
            return HttpResponse('Invalid image')
    else:
        form = ImageForm()
    return render_to_response('sample/upload_image_form.html', {'form': form})
 
def save_file(file, path=''):
    ''' Little helper to save a file
    '''
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()