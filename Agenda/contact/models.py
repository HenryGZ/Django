from django.db import models
from django.utils import timezone

# Create your models here.

'''

id(pk)
first_name (string)
last_name (string)
phone_number (string)
email (email)
created_date (date)
description (text)
category (foreign key)
show (boolean)
owner (foreign key)
picture (imagem)

'''

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)#blank=False, null=False -> não pode ser vazio
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)#auto_now_add=True -> data de criação
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    #picture = models.ImageField(upload_to='contact_pictures', blank=True, null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name #retorna o nome do contato parqa aparecer na página de admin do django
