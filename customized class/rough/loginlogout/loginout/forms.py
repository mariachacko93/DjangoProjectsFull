from  django import forms
from django.forms import ModelForm
from loginout.models import LoginModel

class LoginForm(ModelForm):
    class Meta:
        model=LoginModel
        fields="__all__"