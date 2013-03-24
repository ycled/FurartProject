from django.conf.urls import patterns, url
from furart import views


urlpatterns = patterns('',
    # root
    url(r'^$', views.index, name='index'),
    
    # user management
    url(r'^signin', views.signin, name='signin'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^logout', views.logout, name='logout'),    
    
    # activity
    url(r'^activity/$', views.activity),
    url(r'^activity_post/$', views.activity_post),
    url(r'^activity_post_success/$', views.activity_post_success),
    url(r'^activity_search/$', views.activity_search),
    url(r'^activity_search_result/$', views.activity_search_result),
    url(r'^event_search/$', views.event_search),  
    
    # activity detail
    # ex: /polls/5/
    url(r'^activity/(?P<activity_id>\d+)/$', views.activity_detail, name='detail'),
)
