from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin


from . models import Contrato
from .form import ContratoForm



class ContratoLista(LoginRequiredMixin, ListView):
    login_url= reverse_lazy('login')
    model = Contrato
    template_name = 'contratolist.html'
    
    
    
    
# @login_required
# def contrato_list(request):
#     contrato = Contrato.objects.all()
#     return render (request, 'contratolist.html', { 'contrato': contrato})


class ContratoNew(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Contrato
    fields = [
            'colaborador',
            'contrato',
            'matricula',
            'setor',
            'unidade',
            'datainicio',
        ]
    template_name = 'contratoform.html'
    success_url = reverse_lazy('contrato_list')
    def form_valid(self, form):
        
        form.instance.criadopor = self.request.user
        
        url = super().form_valid(form)
        return url 



# @login_required
# def contrato_new(request):
#     form = ContratoForm(request.POST or None, request.FILES or None)
    
#     if form.is_valid():
#         form.save()
#         return redirect('contrato_list')
#     return render(request, 'contratoform.html', {'form': form})



class ContratoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Contrato
    fields = [
            'colaborador',
            'contrato',
            'matricula',
            'setor',
            'unidade',
            'datainicio',
        ]
    template_name = 'contratoform.html'
    success_url = reverse_lazy('contrato_list')
    
# @login_required
# def contrato_update(request, id):
#     contrato = get_object_or_404(Contrato, pk=id)
#     form = ContratoForm( request.POST or None, request.FILES or None, instance=contrato)
    
#     if form.is_valid():
#         form.save()
#         return redirect('contrato_list')
#     return render(request, 'contratoform.html', {'form': form})


class ContratoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Contrato
    template_name = 'contratodelete.html'
    success_url = reverse_lazy('contrato_list')
# @login_required
# def contrato_delete(request, id):
#     contrato = get_object_or_404(Contrato, pk=id)
    
#     #criar uma tratativa para qnd não puder excluir uma chave estrangeira
#     if request.method == 'POST':
#         contrato.delete()
#         return redirect('contrato_list')
    
#     return render(request, 'contratodelete.html', {'contrato': contrato})
    