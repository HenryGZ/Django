from django.db import models
from django.utils import timezone

# Create your models here.

'''
Contact table

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

'''
Category table

id(pk)

'''

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)#blank=False, null=False -> não pode ser vazio
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)#auto_now_add=True -> data de criação
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True, null=True) #upload_to -> onde a imagem será salva e como será nomeada, com o ano e mês
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name #retorna o nome do contato parqa aparecer na página de admin do django
