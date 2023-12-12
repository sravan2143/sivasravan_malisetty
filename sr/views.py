from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'sr/contact_list.html', {'contacts': contacts})
