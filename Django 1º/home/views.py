from django.shortcuts import render

context ={
    'text': 'Olá home',
}

def home(request):
    return render(
        request, 
        'home/index.html',
        context
        )