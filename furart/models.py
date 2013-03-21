from django.db import models


    
class Activity(models.Model):
    title = models.CharField(max_length=200)
    activitytype = models.CharField(max_length=30)
    organizor = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    detail = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)