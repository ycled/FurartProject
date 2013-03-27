from django import forms


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)    
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    

    

ACTIVIRY_TYPE_CHOICES =  (('Type1', 'Type1'),('Type2', 'Type2'),('Type3', 'Type3'))
#post new activity 
class ActivityForm(forms.Form):
    activitytype = forms.ChoiceField(widget=forms.Select, choices = ACTIVIRY_TYPE_CHOICES,label='Type') 
    title = forms.CharField(required=True)     
    time = forms.DateField(required=True, widget=forms.DateInput(attrs={'format':'%m/%d/%Y'})) 
    organizor = forms.CharField(required=True) 
    location = forms.CharField(required=True)
    #picture = forms.FileField()
    detail = forms.CharField(required=True) 
