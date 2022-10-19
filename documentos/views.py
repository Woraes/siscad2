from ast import Delete
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required

from .models import Documento
from.form import Documentoform


@login_required
def doc_list(request):
    doc = doc.objects.all()
    return render(request,  'doclist.html', {'doc': doc})



@login_required
def doc_new(request):
    form = Documentoform(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('doc_list')
    return render(request, 'docform.html', {'form': form})


@login_required
def doc_update(request, id):
    doc = get_list_or_404(doc, pk=id)
    form = Documentoform( request.POST or None, request.FILES or None, instance=doc)
    
    if form.is_valid():
        form.save()
        return redirect('doc_list')
    return render(request, 'docform.html', {'form': form})



@login_required
def doc_delete(request, id):
    doc = get_list_or_404(doc, pk=id)
    
    
    if request.method == 'POST':
        doc.delete()
        return redirect('doc_list')
    
    return render(request, 'docdelete.html', {'doc': doc})