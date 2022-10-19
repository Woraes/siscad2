
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Colaborador
from.form import Colaboradorform

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin




class ColaboradorLista(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Colaborador
    template_name='colaboradorlist.html'
    
    


# @login_required
# def colaborador_list(request):
#     colaborador = Colaborador.objects.all()
#     return render(request,  'colaboradorlist.html', {'colaborador': colaborador})




class ColaboradorNew(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url=reverse_lazy('login')
    group_required = u'ADM'
    model=Colaborador
    fields = ['nome',
              'nascimento',
              'estadocivil',
              'rg',
              'cpf',
              'pis',
              'cns',
              'ctps',
              'ctpsserie',
              'ctpsuf',
              'genero',
              'phone',
              'email',
              'foto',
              'status',
              ]
    template_name = 'colaboradorform.html'
    success_url =  reverse_lazy ('colaborador_list')
    
    #definir um valor de usuario oculto para saber qual foi o user que fez a postagem
    def form_valid(self, form):
        
        form.instance.criadopor = self.request.user
        
        url = super().form_valid(form)
        return url 
    
    
    
# @login_required
# def colaborador_new(request):
#     form = Colaboradorform(request.POST or None, request.FILES or None)
    
#     if form.is_valid():
#         form.save()
#         return redirect('colaborador_list')
#     return render(request, 'colaboradorform.html', {'form': form})





class ColaboradorUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'ADM','Gestor'
    model = Colaborador
    fields = ['nome',
              'nascimento',
              'estadocivil',
              'rg',
              'cpf',
              'pis',
              'cns',
              'ctps',
              'ctpsserie',
              'ctpsuf',
              'genero',
              'phone',
              'email',
              'foto',
              'status',
              ]
    template_name = 'colaboradorform.html'
    success_url = reverse_lazy('colaborador_list')
    
    


# @login_required
# def colaborador_update(request, id):
#     colaborador = get_object_or_404(Colaborador, pk=id)
#     form = Colaboradorform( request.POST or None, request.FILES or None, instance=colaborador)
    
#     if form.is_valid():
#         form.save()
#         return redirect('colaborador_list')
#     return render(request, 'colaboradorform.html', {'form': form})


class ColaboradorDelete(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'ADM'

    model = Colaborador
    template_name = 'colaboradordelete.html'
    success_url = reverse_lazy('colaborador_list')
    
# @login_required
# def colaborador_delete(request, id):
#     colaborador = get_object_or_404(Colaborador, pk=id)
    
    
#     if request.method == 'POST':
#         colaborador.delete()
#         return redirect('colaborador_list')
    
#     return render(request, 'colaboradordelete.html', {'colaborador': colaborador})