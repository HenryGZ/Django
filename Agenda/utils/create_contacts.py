import os
import sys
import django
from datetime import datetime
from pathlib import Path
from random import choice
from django.conf import settings

#region configurações do django

DJANGO_BASE_DIR = Path(__file__).resolve().parent.parent #diz para o python onde é a pasta raiz para importar para "tras"
NUMBER_OF_OBJECTS = 1000 #numero de contatos a serem criados

sys.path.append(str(DJANGO_BASE_DIR)) #adicionando o caminho do projeto
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings' #dizendo ao django onde está o settings
settings.USE_TZ = False

django.setup()#configurando o django

#endregion

if __name__ == '__main__':
    import faker
    from contact.models import Contact,Category
    #essas importações estão aqui para evitar que o django tente importar antes do 
    #django ser configurado e gerar algum problema
    
    Contact.objects.all().delete() #deletando todos os contatos
    Category.objects.all().delete() #deletando todas as categorias
    
    fake = faker.Faker('pt_BR') #criando um objeto faker para gerar dados falsos
    categories = ['Amigos','Família','Trabalho','Conhecidos'] #categorias que serão criadas
    
    django_categories = [Category(name=name) for name in categories] #lista que vai guardar as categorias criadas no django
    
    for category in django_categories:
        category.save()#salvando as categorias no banco de dados
         
        django_contacts = [] #lista que vai guardar os contatos criados no django
         
        for _ in range(NUMBER_OF_OBJECTS):
            profile = fake.profile()
            email = profile['mail']
            first_name, last_name = profile['name'].split(' ',maxsplit=1) #separando o nome em primeiro e ultimo
            phone_number = fake.phone_number()
            created_date : datetime = fake.date_time_between(start_date='-1y',end_date='now',tzinfo=None)
            description = fake.text(max_nb_chars=100)
            category = choice(django_categories)
             
            django_contacts.append(
                 Contact(
                    first_name = first_name,
                    last_name = last_name,
                    phone = phone_number,
                    email = email,
                    created_date = created_date,
                    description = description,
                    category = category,
                    )
                )
            
    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
                
         