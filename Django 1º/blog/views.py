
from blog.data import posts
from django.shortcuts import render


def blog(request):

    context = {
        # 'text': 'Olá blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request, post_id):

    found_post = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    context = {
        'posts': [found_post]
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):

    context = {
        'text': 'Olá exemplo',
        'title': 'Essa é uma página de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )