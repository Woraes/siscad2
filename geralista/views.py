from csv import excel
from email.mime import application
from multiprocessing import context
import os
from xml.sax import xmlreader
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from geralista.models import Geralista
import datetime
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .form import GeralistaForm
from django.shortcuts import get_object_or_404, get_list_or_404
from attr import validate
from fileinput import close, filename
from xmlrpc.client import DateTime
from attr import validate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from fileinput import close
from xmlrpc.client import DateTime
import xlrd
import xlwt
import pandas as pd
import urllib.parse
from django.views.generic import TemplateView
from django.db import models
# from webdriver_manager.chrome import ChromeDriverManager






  


class GeraListaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Geralista
    template_name = 'geralistalist.html'
    def get_queryset(self):
        self.object_list = Geralista.objects.filter(criadopor=self.request.user)
        
        
        return self.object_list



class GeraListaNew(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url=reverse_lazy('login')
    group_required = u'ADM','Gestor'
    model= Geralista
    fields = ['titulo',
              'menssagem',
              'arquivo1',
              'arquivo2',
              'arquivo3',
        
    ]
    template_name = 'geralistaform.html'
    success_url = reverse_lazy('geralista_list')
    def form_valid(self, form):
        
        form.instance.criadopor = self.request.user
        
        url = super().form_valid(form)
        return url 
    
    
    #mudando o form de acordo com que chamamos 
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
        
            context['titulo'] = 'Criando a Messagem'
            context['botao'] = 'Criar'
        
            return context



class GeraListaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
        login_url = reverse_lazy('login')
        group_required = u'ADM','Gestor'
        model = Geralista
        fields = ['menssagem',
              'arquivo1',
              'arquivo2',
              'arquivo3',
        
    ]
        template_name = 'geralistaform.html'
        success_url = reverse_lazy('geralista_list')
    #    #implementação para apenas o usuario que criou poder editar 1

        def get_object(self, queryset=None):
            self.object = get_object_or_404(Geralista, pk=self.kwargs['pk'], criadopor=self.request.user) 
            return self.object
   
    #mudando o form de acordo com que chamamos 
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
        
            context['titulo'] = 'Edição de Arquivos'
            context['botao'] = 'Salvar'
        
            return context

    

class GeralistaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'ADM','Gestor'
    model = Geralista
    template_name = 'geralistadelete.html'
    success_url = reverse_lazy('geralista_list')



class AcompanhaExe(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'acompanhaexe.html'



    def Waths2(self):
        
            self.lista = 'lista1' 
            print(self.lista)
            tabela = pd.read_excel(self.lista) #criar a lista 
        #campos na ordem do execel
            for linha in tabela.index:
                    nome = tabela.loc[linha, 'nome']
                    telefone = tabela.loc[linha, 'tel']
                    msg = tabela.loc[linha, 'msg']
                    mensagem = tabela.loc[linha, 'mensagem']
                 

    
                    arquivo = tabela.loc[linha, 'arquivo']
                    arquivo2 = tabela.loc[linha, 'arquivo2']
                    arquivo3 = tabela.loc[linha, 'arquivo3']
    
                    caminho = arquivo.replace('img', caminho)
                    caminho2 = arquivo2.replace('img', caminho2)
                    caminho3 = arquivo3.replace('img', caminho3)
    
    # print(caminho)
   
            if horaint <= 12:
                msg = "Bom Dia "
    
            if horaint >= 12:
                msg = "Boa Tarde "  
    
            if horaint >= 18:
                msg = "Boa Noite "    
          
        
    # renomeando a frase 
                texto = mensagem.replace('horario', msg)
 
   
                texto = urllib.parse.quote(texto)
            return (self)       







def Waths(request):
    
        
    navegador = webdriver.Chrome()

#pagina a ser aberta
    navegador.get('https://web.whatsapp.com')

# então Se elementos for menor que 1 da minha lista
    while len(navegador.find_elements(By.ID, 'side')) < 1:
    
            print('Aguardando Scannear QRCode...........')

            time.sleep(3)
            time.sleep(5) 
    tabela = pd.read_excel('Pasta1.xlsx') #criar a lista 
        #campos na ordem do execel
    for linha in tabela.index:
            nome = tabela.loc[linha, 'nome']
            telefone = tabela.loc[linha, 'tel']
            msg = tabela.loc[linha, 'msg']
            mensagem = tabela.loc[linha, 'mensagem']

    
            arquivo = tabela.loc[linha, 'arquivo']
            arquivo2 = tabela.loc[linha, 'arquivo2']
            arquivo3 = tabela.loc[linha, 'arquivo3']
    
            caminho = arquivo.replace('img', caminho)
            caminho2 = arquivo2.replace('img', caminho2)
            caminho3 = arquivo3.replace('img', caminho3)
   
    # print(caminho)
   
            if horaint <= 12:
                msg = "Bom Dia "
    
            if horaint >= 12:
                msg = "Boa Tarde "  
    
            if horaint >= 18:
                msg = "Boa Noite "    
          
        
    # renomeando a frase 
            texto = mensagem.replace('horario', msg)
 
   
            texto = urllib.parse.quote(texto)
    
 
    
    
    
            link = f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'  
            time.sleep(1)
    
            navegador.get(link) 

            while len(navegador.find_elements(By.ID, 'side')) < 1:

                time.sleep(4)
            time.sleep(6)    
    
    
    #verificar se o numero é invalido
            if len ( navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
                navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span' ).click()
        #arquivo imagem
            if arquivo != 'N':
                caminho_completo = os.path.abspath(f'{caminho}')
                caminho_completo2 = os.path.abspath(f'{caminho2}')
                caminho_completo3 = os.path.abspath(f'{caminho3}')
            
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
 
            navegador.find_element(By.XPATH, '//*//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input').send_keys(caminho_completo)
            time.sleep(7)    
            navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
  
            time.sleep(2)   
    if arquivo2 != 'N':    
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click() 
            navegador.find_element(By.XPATH, '//*//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input').send_keys(caminho_completo2)
            time.sleep(3)     
            navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()  


    if arquivo3 != 'N':    
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click() 
            navegador.find_element(By.XPATH, '//*//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input').send_keys(caminho_completo3)     


            time.sleep(7)    
            navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
    time.sleep(6)
    print('-----------------------------Automatizando------------------------------')
    time.sleep(6)  
     
    return (request, {navegador:'navegador'})


MDATA = datetime.datetime.now().strftime('%Y-%m-%d')

def export_msg_xls(model, filename, queryset, columns):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    
    
    wb = xlwt.Workbook(encoding='utf8')
    ws = wb.add_sheet(model)
    
    row_num = 0
    
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    for col_num in range(len(columns)):
        ws.write(row_num,col_num, columns[col_num], font_style)
    
    default_style = xlwt.XFStyle()
    
    rows = queryset
    for row, rowdata in enumerate(rows):
        row_num += 1
        for col, val in enumerate(rowdata):
            ws.write(row_num,col,val, default_style)
    
    

    wb.save(response)
    return response        
 
 
        
def exportar_xlsx(request):
    model = 'Geralista'
    filename = 'tabela_msg.xlsx'
    # _filename = filename.split('.')
    # filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
    queryset = Geralista.objects.all().values_list('titulo',
                                                   'menssagem',
                                                   'arquivo1',
                                                   'arquivo2',
                                                   'arquivo3',
                                                   )
    columns = ('Titulo', 'menssagem', 'arquivo1', 'arquivo2', 'arquivo3')
    response = export_msg_xls(model, filename, queryset, columns)
    return response
    
    
    
   #tenho que fazer um model para capturar as duas tabelas no diretorio da app
def juntartabelas(response,):
    tabelamsg = pd.read_excel ('tabela_msg.xlsx')
    tabelapessoas = pd.read_excel('311.xlsx')
    lista1 = pd.concat([tabelamsg,tabelapessoas], ignore_index=True)
    lista1 = lista1.drop(['nome'])
    # for linha in lista1.index:
    #     nome = lista1.loc[linha, 'nome']
    #     telefone = lista1.loc[linha, 'tel']
    #     msg = lista1.loc[linha, 'msg']
    #     mensagem = lista1.loc[linha, 'mensagem']
    
    #     arquivo = lista1.loc[linha, 'arquivo']
    #     arquivo2 = lista1.loc[linha, 'arquivo2']
    #     arquivo3 = lista1.loc[linha, 'arquivo3']
    
        # caminho = arquivo.replace('img', caminho)
        # caminho2 = arquivo2.replace('img', caminho2)
        # caminho3 = arquivo3.replace('img', caminho3)     
    response = export_msg_xls(filename)
    return response

 