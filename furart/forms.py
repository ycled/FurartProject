from django import forms


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    

class MessageForm(forms.Form): 
    name = forms.CharField(required=True) 
    email = forms.EmailField(required=True) 
    homepage = forms.URLField(required=False) 
    title = forms.CharField(required=True) 
    content = forms.CharField(required=True)
    

ACTIVIRY_TYPE_CHOICES =  (('A', 'a'),('B', 'b'))
#post new activity 
class ActivityForm(forms.Form):
    activitytype = forms.ChoiceField(widget=forms.Select, choices = ACTIVIRY_TYPE_CHOICES,label='Type') 
    title = forms.CharField(required=True)     
    time = forms.CharField(required=True) 
    organizor = forms.CharField(required=True) 
    location = forms.CharField(required=True)
    picture = forms.FileField()
    detail = forms.CharField(required=True) 