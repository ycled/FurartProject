from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)


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
