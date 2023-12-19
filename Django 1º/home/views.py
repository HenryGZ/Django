# from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render

# def home(request):
#     print('home')
#     return HttpResponse('home do app')


#não esquecer de registrar no installed apps no arquivo settings do projeto

context ={
    'user': 'Fulano de Tal',
    'chave': 'valor'
}

def home(request):
    return render(
        request, 
        'home/index.html',
        context)