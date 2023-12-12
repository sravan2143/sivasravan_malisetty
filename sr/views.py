from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm  # make sure you have created this form in forms.py

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'sr/contact_form.html', {'form': form})
