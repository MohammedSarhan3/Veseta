from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm  

class UserCreationForm(UserCreationForm):
    username=forms.CharField(label='الإسم')
    first_name=forms.CharField(label='الإسم الأول')
    last_name=forms.CharField(label='الإسم الأخير')
    email=forms.EmailField(label='البريد الإلكتروني')
    password1=forms.CharField(label='كلمة السر',widget=forms.PasswordInput(),min_length=8)
    password2=forms.CharField(label='تأكيد كلمة السر',widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
class LoginForm(forms.ModelForm):
    username= forms.CharField(label="الإسم")
    password= forms.CharField(label="كلمة المرور", widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','password')

class Update_User_Form(forms.ModelForm):
    first_name=forms.CharField(label='الإسم الأول')
    last_name=forms.CharField(label='الإسم الأخير')
    email=forms.EmailField(label='البريد الإلكتروني')

    class Meta:
        model= User
        fields=('first_name','last_name','email'

        )    

class Update_Profile_Form(forms.ModelForm):
  

    class Meta:
        model= Profile
        fields=('name','subtitle','adress',
        'adress_detail',
        'number_phone',
        'working_hours',
        'wating_time',
        'spcalist_doctor',
        
        'type',
        'who_i',
        'doctor',
        'price',

        )    