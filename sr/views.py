from django.shortcuts import get_object_or_404, render
from .models import Contact

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'sr/contact_detail.html', {'contact': contact})
from django.shortcuts import redirect, render, get_object_or_404
from .models import Contact
from .forms import ContactForm  # Assuming you have a ContactForm in forms.py

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'sr/contact_form.html', {'form': form})

from django.shortcuts import redirect, render, get_object_or_404
from .models import Contact

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'sr/contact_confirm_delete.html', {'contact': contact})