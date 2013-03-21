from django import forms

#sample!! to be removed!!!
class MessageForm(forms.Form): 
    name = forms.CharField(required=True) 
    email = forms.EmailField(required=True) 
    homepage = forms.URLField(required=False) 
    title = forms.CharField(required=True) 
    content = forms.CharField(required=True)
    

#post new activity 
class ActivityForm(forms.Form): 
    title = forms.CharField(required=True) 
    activitytype = forms.CharField(required=True) 
    organizor = forms.CharField(required=True) 
    location = forms.CharField(required=True) 
    detail = forms.CharField(required=True) 
    time = forms.CharField(required=True) 