from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('blog')
    context = {
        'text': 'Olá blog'
    }
    return render(request, 'blog/index.html', context)

def example(request):
    print('example')
    
    context = {
        'text': 'Olá example',
        'title':'essa é a pagina example'
    }
    
    return render(request, 'blog/example.html', context)