from django.urls import path,include
from .views import doctors_detail,doctors_list


app_name='accounts'
urlpatterns = [
path('Doctors/', doctors_list,name='doctors_list'),
path('<slug:slug>/', doctors_detail,name='doctors_detail'),
]
