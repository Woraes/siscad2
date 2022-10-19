from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Unidade
from .forms import Unidadeform
# #importa para criar as vizualizaçoes do que foi criado no models.py
# from django.views.generic import CreateView
# #importa os models criados no models.py
# from .models import unidade, Unidade
# #importa para redicecionar para uma url html
# from django.urls import reverse_lazy

# #Criando view 
# #class NomeSemelhante(CreateView):
# #model = nome do model importado
# # fields = ['campos dos models que deseja exibir']
# #template_name = 'nomedoapp/nomehtml.html' caminho/seudestino.html
# #success_url = reverse_lazy('index') redirecionar para este html que foi definido esse nome
# class unidadecreate(CreateView):
#     model = unidade
#     fields = [
#         'nome', 
#         'sigla', 
#         'descricao', 
#         'estado', 
#         'cidade', 
#         'municipio',
#         'telefone', 
#         ]
#     template_name = 'unidadeform.html'
#     success_url = reverse_lazy('index')
  
  
# class Unidadecreate(CreateView):
#     model = Unidade
#     fields = [
#         'nome', 
#         'unidade', 
#         'ramal',
#         'status',
#         'descricao',
        
#     ]    
    
#     template_name = 'unidadeform.html'
#     success_url = reverse_lazy('index')




# @login_required
# def cliente_list(request):
#     cliente = unidade.objects.all()
#     return render(request,  'cliente.html', {'clientes': cliente})





# @login_required
# def pessoa_update(request, id):
#     pessoa = get_object_or_404(Pessoa, pk=id)
#     form = PessoaForm( request.POST or None, request.FILES or None, instance=pessoa)
    
#     if form.is_valid():
#         form.save()
#         return redirect('pessoa_list')
#     return render(request, 'pessoa_form.html', {'form': form})


# @login_required
# def pessoa_delete(request, id):
#     pessoa = get_object_or_404(Pessoa, pk=id)
    
    
#     if request.method == 'POST':
#         pessoa.delete()
#         return redirect('pessoa_list')
    
#     return render(request, 'pessoa_delete_confirm.html', {'pessoa': pessoa})





@login_required
def unidade_list(request):
    unidade = Unidade.objects.all()
    return render(request, 'unidadelist.html', {'unidade': unidade})





@login_required
def unidade_new(request):
    form = Unidadeform(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('unidade_list')
    return render(request, 'unidadeform.html', {'form': form})


@login_required
def unidade_update(request, id):
    unidade = get_object_or_404(Unidade, pk=id)
    form = Unidadeform( request.POST or None, request.FILES or None, instance=unidade)
    
    if form.is_valid():
        form.save()
        return redirect('unidade_list')
    return render(request, 'unidadeform.html', {'form': form})



@login_required
def unidade_delete(request, id):
    unidade = get_object_or_404(Unidade, pk=id)
    
    
    if request.method == 'POST':
        unidade.delete()
        return redirect('unidade_list')
    
    return render(request, 'unidadedelete.html', {'unidade': unidade})