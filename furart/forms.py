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
        

    
    
    
########################################################################    

# post new activity
ACTIVIRY_TYPE_CHOICES =  (('Type1', 'Type1'),('Type2', 'Type2'),('Type3', 'Type3'))
ACTIVIRY_TIME_CHOICES =  (('00:00', '00:00'),('01:00', '01:00'),('02:00', '02:00'))
 
class ActivityForm(forms.Form):
    
    activitytype = forms.ChoiceField(widget=forms.Select,
                                     choices = ACTIVIRY_TYPE_CHOICES,label='Type') 
    title = forms.CharField(required=True)     
    
    # date and time
    start_date = forms.DateField(required=True,
                           widget=forms.DateInput(attrs={'format':'%m/%d/%Y'})) 
    start_time = forms.ChoiceField(widget=forms.Select,
                                     choices = ACTIVIRY_TIME_CHOICES,label='Start Time') 
    end_date = forms.DateField(required=True,
                           widget=forms.DateInput(attrs={'format':'%m/%d/%Y'})) 
    end_time = forms.ChoiceField(widget=forms.Select,
                                     choices = ACTIVIRY_TIME_CHOICES,label='End Time') 
    
    organizer = forms.CharField(required=True) 
    location = forms.CharField(required=True)
    poster = forms.FileField(label="Select a poster for you activity",
                             help_text="max size 1M")
    detail = forms.CharField(widget=forms.Textarea)