from django import forms
from django.core import validators
from .models import Accounts,Articles,Articles_Details,Comments
import re

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Accounts
        fields = "__all__"
  
class LoginForm(forms.Form):
    Username = forms.CharField(max_length='128')
    Passowrd = forms.CharField(max_length= '32',widget=forms.PasswordInput())

    def clean(self,):
        super(LoginForm,self).clean()
        Username = self.cleaned_data.get("Username")
        Password = self.cleaned_data.get("Password")
        try:
            user = Accounts.objects.get(Username=Username)
            if Password!=user.Password:
                self._errors['Password'] = self._error_class['Password Doesn\'t Match']
        except:
            self._error["Username"] = self._error_class[f"User with {Username} USername Can't be Found"]
        finally:    
            return self.cleaned_data


