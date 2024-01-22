from django.shortcuts import render
from contact.models import Contact
from django.http import Http404

from django.shortcuts import get_object_or_404

def index(request):
    
    #pega os contatos da tabela onde o campo show é true e ordena por id
    contacts = Contact.objects.filter(show=True).order_by('id')[:10]
    
    #print(contacts.query) mostra a query que está sendo executada
    
    context = {
        'contacts': contacts,
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
    }
    
    return render(
        request,
        'contact/contact.html',
        context
        )