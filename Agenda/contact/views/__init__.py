#usado par ser a primeira coisa a ser executada quando esse pacote 
#for importado e executado

'''
como esse arquivo é executado primeiro, as importaçãoes
parecerão que são diretamente do diretório contact, mas na 
verdade são do arquivoque está sendo importado
'''
from .contact_views import *
from .contact_forms import *
from .user_forms import *

#as views são importadas para serem usadas no arquivo urls.py
#elas não podem ter nomes de funções iguais




