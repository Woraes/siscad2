from multiprocessing import context
from urllib import response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required

from numpy import fix
from psycopg2 import DATETIME

from.models import PessoaModel
from .form import Pessoaform
import xlrd
import xlwt
from datetime import date
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404








class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = PessoaModel
    template_name = 'pessoalist.html'
    
    #definindo para que cada usuario veja apenas os seus cadastros
    def get_queryset(self):
        self.object_list = PessoaModel.objects.filter(criadopor=self.request.user)
        
        
        return self.object_list
    
    

class PessoaNew(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = PessoaModel
    fields = [
            'nome',
            'genero',
            'nascimento',
            'idade',
            'estadocivil',
            'escolaridade',
            'telefone',
            'email',
            'status',
            'estado',
            'cidade'
        ]    
    template_name = 'pessoaform.html'
    success_url = reverse_lazy('pessoa_list')
    def form_valid(self, form):
        
        form.instance.criadopor = self.request.user
        
        url = super().form_valid(form)
        return url 

    
    
     
    #aqui passamos para o front os dados que queremos em cada form
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = 'Cadastro de Pessoas'
        context['botao'] = 'Cadastrar'
        context['teste'] = 'ooioioioi' 
        return context
    
class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'ADM','Gestor','User'
    model = PessoaModel
    fields = [
            'nome',
            'genero',
            'nascimento',
            'idade',
            'estadocivil',
            'escolaridade',
            'telefone',
            'email',
            'status',
            'estado',
            'cidade'
        ]   
    template_name = 'pessoaform.html'
    success_url = reverse_lazy('pessoa_list')
    
    
    #implementação para apenas o usuario que criou poder editar 1
    # def get_object(self, queryset=None):
    #     self.object = PessoaModel.objects.get(pk=self.kwargs['pk'], criadopor=self.request.user) 
    #     return self.object
    
    
    #modo de editar 2
    def get_object(self, queryset=None):
        self.object = get_object_or_404(PessoaModel, pk=self.kwargs['pk'], criadopor=self.request.user) 
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = 'Editar Pessoa'
        context['botao'] = 'Salvar'
        
        return context




class PessoaDelete(GroupRequiredMixin ,LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'ADM'
    model = PessoaModel
    template_name = 'pessoadelete.html'
    success_url = reverse_lazy('pessoa_list')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(PessoaModel, pk=self.kwargs['pk'], criadopor=self.request.user) 
        return self.object








 
 
 

        