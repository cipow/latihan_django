from django.shortcuts import render
from .forms import cobaForm, lagiForm

def publish(request):
    return render(request, 'publish/index.html',{})

def publish_page(request, page):
    title = 'page '+str(page)
    no = str(page)
    form = lagiForm()
    return render(request, 'publish/page.html',{
        'title':title,
        'no':no,
        'form':form
    })
