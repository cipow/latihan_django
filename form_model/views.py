from django.shortcuts import render
from .forms import ContactMeForm

def coba(request, template_name = 'form_model/form.html'):
    form = ContactMeForm()
    return render(request, template_name, {'form':form})
