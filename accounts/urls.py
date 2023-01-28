from django.urls import path
from .views import doctors_detail,doctors_list,user_login


app_name='accounts'
urlpatterns = [
        path('Doctors/', doctors_list,name='doctors_list'),
        path('Login/', user_login,name='Login'),
        path('<slug:slug>/', doctors_detail,name='doctors_detail'),

]