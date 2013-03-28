from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=50)


class Activity(models.Model):
    uploader = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    activitytype = models.CharField(max_length=30)
    organizor = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    poster = models.FileField(upload_to='documents')
    detail = models.CharField(max_length=500)
    #time = models.DateTimeField(auto_now_add=True)
    time = models.DateField()
    
    def is_today(self):
        return self.time - timezone.now() <= datetime.timedelta(days=0)
    
    def is_tomorrow(self):
        return self.time - timezone.now() <= datetime.timedelta(days=1)
