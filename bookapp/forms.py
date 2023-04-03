from django import forms
from django.contrib.auth.models import User

from .models import *


class regform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class logform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)


class bookupform(forms.ModelForm):
    class Meta:
        model=bookupmodel
        fields="__all__"