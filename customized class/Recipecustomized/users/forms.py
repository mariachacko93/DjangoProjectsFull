from django.contrib.auth.forms import UserCreationForm,User
from django import forms

class registerForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]


class loginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)

