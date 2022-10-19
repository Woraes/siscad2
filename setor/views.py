from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor
from.form import Setorform




@login_required
def setor_list(request):
    setor = Setor.objects.all()
    return render(request,  'setorlist.html', {'setor': setor})



@login_required
def setor_new(request):
    form = Setorform(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('setor_list')
    return render(request, 'setorform.html', {'form': form})


@login_required
def setor_update(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = Setorform( request.POST or None, request.FILES or None, instance=setor)
    
    if form.is_valid():
        form.save()
        return redirect('setor_list')
    return render(request, 'setorform.html', {'form': form})



@login_required
def setor_delete(request, id):
    setor = get_object_or_404(Setor, pk=id)
    
    #criar uma tratativa para qnd não puder excluir uma chave estrangeira
    if request.method == 'POST':
        setor.delete()
        return redirect('setor_list')
    
    return render(request, 'setordelete.html', {'setor': setor})