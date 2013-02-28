from django.contrib.auth.models import User
from django import forms


class SignupForm(forms.Form):
    Username = forms.CharField(max_length=255, label="Username")
    FirstName = forms.CharField(max_length=255, label="First Name")
    LastName = forms.CharField(max_length=255, label="Last Name")
    Email = forms.CharField(max_length=255, label="E-Mail Address")
    Password = forms.CharField(max_length=255, label="Password", widget=forms.PasswordInput)
    Password2 = forms.CharField(max_length=255, label="Repeat Password", widget=forms.PasswordInput)

    
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username is already in use.Please choose another.")
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("You must type the same password each time")
        return self.cleaned_data
        
    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
        return new_user
