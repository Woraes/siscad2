from asyncio import mixins
import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# class IndexView(LoginRequiredMixin, TemplateView):
#     login_url = reverse_lazy('login')
#     template_name = 'index.html'
    




class Sobre(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'sobre.html'


class Ajuda(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'ajuda.html'



class Registrar(TemplateView):
    
    template_name = 'registrar.html'
    
 
 

       
        

@login_required   
def index(request):
    
    
    
    
   
    data = datetime.date.today()
    hora = (datetime.datetime.now())
    horaint = int(hora.strftime('%H'))
    print( '....................Hoje é Dia : ',data, '....................')
    print(hora)
    print('Hora:',horaint)
    if horaint <= 12:
            msg = "Bom Dia"
         
    
    if horaint >= 12:
            msg = "Boa Tarde" 
         
    
    if horaint >= 18:
            msg = "Boa Noite"    
        
    print(msg) 
    context = msg
       
    return render(request, 'index.html', {'context':context, 'data': data})