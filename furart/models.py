from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    homepage = models.URLField()
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=20)
    
    
class Activity(models.Model):
    title = models.CharField(max_length=200)
    activitytype = models.CharField(max_length=30)
    organizor = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    detail = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)