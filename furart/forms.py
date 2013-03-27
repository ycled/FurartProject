from django import forms

from furart.models import User


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)    
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'%s already exists' % username )
        

class MessageForm(forms.Form): 
    name = forms.CharField(required=True) 
    email = forms.EmailField(required=True) 
    homepage = forms.URLField(required=False) 
    title = forms.CharField(required=True) 
    content = forms.CharField(required=True)
    

ACTIVIRY_TYPE_CHOICES =  (('A', 'a'),('B', 'b'))
# post new activity 
class ActivityForm(forms.Form):
    activitytype = forms.ChoiceField(widget=forms.Select,
                                     choices = ACTIVIRY_TYPE_CHOICES,label='Type')
    title = forms.CharField(required=True)
    time = forms.CharField(required=True)
    organizor = forms.CharField(required=True)
    location = forms.CharField(required=True)
    poster = forms.FileField(label="Select a poster for you activity",
                             help_text="max size 1M")
    detail = forms.CharField(required=True) 
