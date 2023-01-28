from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username= forms.CharField(label="الإسم")
    password= forms.CharField(label="كلمة المرور", widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','password')