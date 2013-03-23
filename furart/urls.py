from django.conf.urls import patterns, url
from furart import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'signup.html', views.signup, name='signup'),
    
    url(r'^activity/$', views.activity),
    
    
    url(r'^activity_post/$', views.activity_post),
    url(r'^activity_post_success/$', views.activity_post_success),
    url(r'^activity_search/$', views.activity_search),
    url(r'^activity_search_result/$', views.activity_search_result),
    url(r'^event_search/$', views.event_search),  
    
    
    # create new evnet
    url(r'^event_create/$', views.event_create),
    url(r'^event_create_success/$', views.event_create_success),
    
)
