from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.

def doctors_list(request):
    doctors =User.objects.all()
    return render(request,"user/doctors_list.html",{
        'doctors':doctors,
    })


def doctors_detail(request,slug):
    doctors_detail =Profile.objects.get(slug=slug)
    return render(request,"user/doctors_detail.html",{
        'doctors_detail':doctors_detail,
    })

def user_login(request):
    if request.methd=='POST':
        form=LoginForm()
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts:doctors_list')
    else:
        form=LoginForm()

    return render(request,"user/login.html",{
        'form':form
    })