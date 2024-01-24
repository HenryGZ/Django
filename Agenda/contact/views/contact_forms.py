from django.shortcuts import render
from contact.forms import ContactForm
from django.shortcuts import redirect

def create(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
                
        context = {
            'form' : ContactForm(request.POST)
        }
        
        if form.is_valid():
            # contact = form.save(commit=False) # commit=False para não salvar no banco de dados
            form.save(commit=True)#commit=True para salvar no banco de dados, ele é true por defautl
            return redirect('contact:create') 
            
        return render(
            request,
            'contact/create.html',
            context
            )
    else:  
        context = {
            'form' : ContactForm(),
        }
        
        
        return render(
            request,
            'contact/create.html',
            context
            )