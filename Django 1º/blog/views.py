from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('blog')
    return render(request, 'blog/index.html')

def example(request):
    print('example')
    return render(request, 'blog/example.html')