from django import forms


ACTIVIRY_TYPE_CHOICES =  (('A', 'a'),('B', 'b'))



#post new activity 
class ActivityForm(forms.Form):
    activitytype = forms.ChoiceField(widget=forms.Select, choices = ACTIVIRY_TYPE_CHOICES,label='Type') 
    title = forms.CharField(required=True)     
    time = forms.CharField(required=True) 
    organizor = forms.CharField(required=True) 
    location = forms.CharField(required=True) 
    detail = forms.CharField(required=True) 
