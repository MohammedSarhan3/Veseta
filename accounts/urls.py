from django.urls import path
from .views import doctors_detail,doctors_list,user_login,myprofile,Signup,update_profile


app_name='Accounts'
urlpatterns = [
        path('Doctors/', doctors_list,name='doctors_list'),
        path('Login/', user_login,name='Login'),
        path('Signup/', Signup ,name='Signup'),
        path('myprofile/', myprofile,name='myprofile'),
        path('update_profile/', update_profile,name='update_profile'),

        path('<slug:slug>/', doctors_detail,name='doctors_detail'),

]