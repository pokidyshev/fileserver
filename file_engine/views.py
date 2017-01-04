import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Document
from .forms import DocumentForm
from .encoding import encode, decode


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
    file_path = obj.document.path

    if not os.path.exists(file_path):
        raise Http404

    with open(file_path, 'rb') as fp:
        response = HttpResponse(
            fp.read(),
            content_type='application/force-download'
        )
        response['Content-Disposition'] = ('inline; filename=' +
                                           os.path.basename(file_path))
        return response
