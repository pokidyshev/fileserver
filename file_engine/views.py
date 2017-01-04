from django.shortcuts import render, redirect, get_object_or_404

from .models import Document
from .forms import DocumentForm
from .encoding import encode, decode


def home(request):
    documents = Document.objects.all()
    return render(request, 'file_engine/home.html', {
        'documents': documents
    })


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return redirect('/%s' % encode(file.id))
    else:
        form = DocumentForm()

    return render(request, 'file_engine/upload.html', {
        'form': form
    })


def details(request):
    encoded_id = request.path.split('/')[-1]
    obj = get_object_or_404(Document, pk=decode(encoded_id))
    return render(request, 'file_engine/details.html', {
        'obj': obj
    })
