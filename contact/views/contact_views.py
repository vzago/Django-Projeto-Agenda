from django.shortcuts import render, get_object_or_404,redirect
from contact.models import Contact
from django.db.models import Q
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[10:20]
    
    context = {
        'contacts': contacts,
        'site_title' : 'Contatos - ',
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )
def search(request):
    search_value = request.GET.get('q', '').strip() # Get the search value from the request
    
    if search_value == '':
        return redirect('contact:index') # Redirect to index page
    
    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains= search_value) | # Search in first_name or
            Q(last_name__icontains= search_value) | # Search in last_name
            Q(phone__icontains= search_value) | # Search in last_name
            Q(email__icontains= search_value)  # Search in email
            )\
        .order_by('-id')    
    
    context = {
        'contacts': contacts,
        'site_title' : 'Search - ', 
        'search_value': search_value,
    }
    
    return render( 
        request,
        'contact/index.html',
        context
    ) # render the index page with the context
    
def contact(request, contact_id):
    # single_contact = Contact.objects.get(pk = contact_id)
    single_contact = get_object_or_404(Contact, pk=contact_id,show=True)
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} -'
    
    context = {
        'contact': single_contact,
        'site_title' : site_title,
        
    }
    
    return render(
        request,
        'contact/contact.html',
        context
    )