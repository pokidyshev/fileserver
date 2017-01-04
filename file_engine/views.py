import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.conf import settings

from .models import Document
from .forms import DocumentForm
from .encoding import encode, decode


def home(request):
    documents = Document.objects.all()
    return render(request, 'file_engine/home.html', {
        'documents': documents,
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
        'form': form,
    })


def details(request):
    encoded_id = request.path.split('/')[-1]
    obj = get_object_or_404(Document, pk=decode(encoded_id))
    return render(request, 'file_engine/details.html', {
        'obj': obj,
        'encoded_id': encoded_id,
    })


def download(request):
    encoded_id = request.path.split('/')[-1]
    obj = get_object_or_404(Document, pk=decode(encoded_id))
    file_path = os.path.join(settings.MEDIA_ROOT, obj.document.name)

    if not os.path.exists(file_path):
        raise Http404

    with open(file_path, 'rb') as fh:
        response = HttpResponse(
            fh.read(),
            content_type='application/force-download'
        )
        response['Content-Disposition'] = ('inline; filename=' +
                                           os.path.basename(file_path))
        return response
