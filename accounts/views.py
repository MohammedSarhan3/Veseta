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


def doctors_detail(request,slug):
    doctors_detail =Profile.objects.get(slug=slug)
    return render(request,"user/doctors_detail.html",{
        'doctors_detail':doctors_detail,
    })


def Signup(request):
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect('accounts:doctors_list')
    else:
        form =UserCreationForm()
    return render(request,"user/signup.html",{
        'form':form
    })
    
def user_login(request):
    if request.method=='POST':
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
    
@login_required()
def myprofile(request):
    return render(request,"user/myprofile.html",{
        
    })

def update_profile(request):
    user_form=Update_User_Form(instance=request.user)
    profile_form=Update_Profile_Form(instance=request.user.profile)
    
    if request.method=='POST':
        user_form=Update_User_Form(request.POST,instance=request.user)
        profile_form=Update_Profile_Form(request.POST,request.FILES,instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('accounts:myprofile')

       

    return render(request,"user/updatee_profile.html",{
        'user_form':user_form,'profile_form':profile_form
    })