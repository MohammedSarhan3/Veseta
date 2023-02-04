from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm,UserCreationForm,Update_User_Form,Update_Profile_Form
from django.contrib.auth import authenticate,login
# Create your views here.

def doctors_list(request):
    doctors =User.objects.all()
    return render(request,"user/doctors_list.html",{
        'doctors':doctors,
    })

