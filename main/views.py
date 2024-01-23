from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('main:contact')
    ctx = {
        'form': form
    }
    return render(request, 'main/contact.html', ctx)