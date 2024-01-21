from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
class Category(models.Model):
    
    class Meta: #configurações do nome da classe dentro do admin
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
    
    name = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)#blank=False, null=False -> não pode ser vazio
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)#auto_now_add=True -> data de criação
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True, null=True) #upload_to -> onde a imagem será salva e como será nomeada, com o ano e mês
    
    #esse owner será o usuário que criou o contato
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True ) #on_delete -> o que acontece com os contatos quando o usuário for deletado
    
    #declaração de chave strangeira: models.ForeignKey('nome da tabela', on_delete=models.CASCADE)
    #o campo tem que poder receber nll e ser opcional, por isso o blank=True, null=True, para que possa receber null quando for deletada
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) #on_delete -> o que acontece com os contatos quando a categoria for deletada
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name #retorna o nome do contato parqa aparecer na página de admin do django
