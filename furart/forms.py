from django import forms

from furart.models import User

import hashlib



class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(u'username %s does not exist' % username )
    
        password = self.cleaned_data['password']
        hashed_password = hashlib.md5(password).hexdigest()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(u'username %s does not exist' % username )
        if user.password != hashed_password:
            raise forms.ValidationError(u'password error' )
        return self.cleaned_data
        

class SignupForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)    
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'username %s already exists' % username )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'email %s already exists' % email )

    def clean(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        hashed_password = hashlib.md5(password1).hexdigest()
        self.cleaned_data['password'] = hashed_password

        return self.cleaned_data


ACTIVIRY_TYPE_CHOICES =  (('Type1', 'Type1'),('Type2', 'Type2'),('Type3', 'Type3'))
# post new activity 
class ActivityForm(forms.Form):
    activitytype = forms.ChoiceField(widget=forms.Select,
                                     choices = ACTIVIRY_TYPE_CHOICES,label='Type') 
    title = forms.CharField(required=True)     
    time = forms.DateField(required=True,
                           widget=forms.DateInput(attrs={'format':'%m/%d/%Y'})) 
    organizor = forms.CharField(required=True) 
    location = forms.CharField(required=True)
    poster = forms.FileField(label="Select a poster for you activity",
                             help_text="max size 1M")
    detail = forms.CharField(required=True) 
