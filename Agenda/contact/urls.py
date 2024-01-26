from django.urls import path
from contact import views 

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    #CRUD operations
    path('contact/detail/<int:contact_id>/', views.contact, name='contact'), #read
    path('contact/create/', views.create, name='create'), #create
    path('contact/update/<int:contact_id>/', views.update, name='update'), #update
    path('contact/delete/<int:contact_id>/', views.delete, name='delete'), #delete
    
    #create user
    path('user/register/', views.register, name='register'),
]
