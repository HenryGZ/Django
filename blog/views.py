from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path
from django.http.response import HttpResponse

#HTTP é baseado em request e response
#MVC - Model View Controller

def myView(request):
    return HttpResponse("View")

def home(request):
    return HttpResponse("Home")