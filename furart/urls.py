from django.conf.urls import patterns, url

from furart import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'signup.html', views.signup, name='signup')
)
