from django.contrib import admin
from contact.models import Contact
from contact import models

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): 
    
    '''existem muitas opções de configuração para o admin,
    para saber mais acesse: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/'''
    
    list_display = ('id','first_name','last_name','phone',) # Campos que serão exibidos na listagem
    ordering = ('id',) # Ordenação dos campos pelo id
    #search_fields = ('first_name','last_name','phone_number',) # Campos que serão pesquisados
    #list_filter = ('created_date',) # Campos que serão filtrados
    list_per_page = 30 # Quantidade de registros por página
    list_max_show_all = 100 # Quantidade máxima de registros a serem exibidos
    list_display_links = ('id','first_name',) # Campos que serão exibidos como links
    
    @admin.register(models.Category)
    class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name',)
        ordering = ('id',)