from django.urls import path,include
from .views import main


app_name='accounts'
urlpatterns = [
path('main/', main),
]
