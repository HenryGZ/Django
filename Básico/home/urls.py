from django.urls import path
from . import views # . significa que está na mesma pasta

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'), 
]