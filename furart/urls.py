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
    #url(r'^activity/$', views.activity),
    
    # post new acticity
    url(r'^activity_post/$', views.activity_post),
    url(r'^activity_post_success/$', views.activity_post_success),

    # activity detail
    # ex: /activity/1/
    url(r'^activity/(?P<activity_id>\d+)/$', views.activity_detail, name='detail'),   
    # edit activity
    url(r'^activity/(?P<activity_id>\d+)/edit/$', views.activity_edit, name='edit'),
    url(r'^activity_edit_success/$', views.activity_edit_success),   
    
    url(r'^profile/$', views.profile, name='profile'),
    
    # search activity
    #url(r'^activity_search/$', views.activity_search),
    #url(r'^activity_search_result/$', views.activity_search_result),

    
    
    # search event
    url(r'^events/(?P<timerange>\w+)-(?P<activity_type>\w+)-(?P<location>\w+)/$', views.event_search, name='search'),

)
