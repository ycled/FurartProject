from django.conf.urls import patterns, url

from furart import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    
    url(r'^activity/$', views.activity),
    url(r'^message/$', views.message),
    url(r'^activity_post/$', views.activity_post),
    url(r'^activity_post_success/$', views.activity_post_success),
    url(r'^activity_search/$', views.activity_search),
    url(r'^activity_search_result/$', views.activity_search_result), 
)
