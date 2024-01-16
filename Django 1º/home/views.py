from django.shortcuts import render

context ={
    'user': 'Fulano de Tal',
    'chave': 'valor'
}

def home(request):
    return render(
        request, 
        'home/index.html',
        context)