from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document
from .forms import DocumentForm

def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            height = request.POST['height']
            width = request.POST['width']
            docfile = request.FILES['docfile']
            final_docfile = request.FILES['fnal_docfile']
            newdoc = Document(docfile=docfile, final_docfile=final_docfile, height=height, width=width)
            newdoc.save()
            # Redirect to the document list after POST
            return render(request, 'myapp/index.html', {'Success': 'Uploaded Successfully! Thank you for uploading..'})
    else:
        return render(request, 'myapp/index.html')

def list(request):
    documents = Document.objects.all().order_by('-id')
    return render(request, 'myapp/list.html', {'documents': documents})

