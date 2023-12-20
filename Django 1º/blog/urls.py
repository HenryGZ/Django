from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('example/', views.example, name = 'example'),
]