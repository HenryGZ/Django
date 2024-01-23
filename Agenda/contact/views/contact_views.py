from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render


def index(request):
    
    #pega os contatos da tabela onde o campo show é true e ordena por id
    contacts = Contact.objects.filter(show=True).order_by('id')
    
    #cria e define a paginação da lista de contatos
    paginator = Paginator(contacts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    #print(contacts.query) mostra a query que está sendo executada
    context = {
        'page_obj': page_obj,
        'site_title':'Contatos -'
    }
    
    return render(
        request,
        'contact/index.html',
        context
        )

def contact(request, contact_id):
    
    #pega o contato da tabela onde o campo show é true e o id é igual ao id passado na url
    #single_contact = Contact.objects.get(pk = contact_id, show=True)
    
    #o get pode trazer um problema de página não encontrada, então usamos o filter que retorna uma lista
    #e pegamos o primeiro elemento da lista
    # single_contact = Contact.objects.filter(pk = contact_id, show=True).first()
    
    # if single_contact is None:
    #     raise Http404('Contato não encontrado')
    
    #pode ser feita assim, mas o django possui já um atalho para esse tipo de problema:
    single_contact = get_object_or_404(Contact, pk = contact_id, show=True)
    
    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.name} {single_contact.last_name} -'
    }
    
    return render(
        request,
        'contact/contact.html',
        context
        )

def search(request):
    search_value = request.GET.get('q', '').strip()
        
    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)
        )
    
    #cria e define a paginação da lista de contatos
    paginator = Paginator(contacts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    #print(contacts.query) mostra a query que está sendo executada
    
    context = {
        'page_obj': page_obj,
        'site_title':'Search -',
        'search_value': search_value,    #passa o valor tratado da busca para o template, permite que o valor fique no search e não seja limpo
    }
    
    return render(
        request,
        'contact/index.html',
        context
        )