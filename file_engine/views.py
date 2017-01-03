from django.shortcuts import render, redirect

from file_engine.models import Document
from file_engine.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'file_engine/home.html', {
        'documents': documents
    })


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

    return render(request, 'file_engine/upload.html', {
        'form': form
    })
