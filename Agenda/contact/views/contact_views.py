from django.shortcuts import render
from contact.models import Contact

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
