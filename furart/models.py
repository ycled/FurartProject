from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=50)


class Activity(models.Model):
    uploader = models.CharField(max_length=200)
    
    title = models.CharField(max_length=200)
    activitytype = models.CharField(max_length=30)
    organizer = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    poster = models.FileField(upload_to='posters/%Y/%m/%d')
    detail = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.CharField(max_length=20) ###TODO: time field type
    end_time = models.CharField(max_length=20)

