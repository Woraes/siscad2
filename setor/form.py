from django.forms import ModelForm
from.models import Setor
from django.urls import reverse_lazy




class Setorform(ModelForm):
    class Meta:
        model = Setor
        fields = [
            'nome', 
            'sigla', 
            'descricao', 
            'estado', 
            'cidade', 
            'municipio',
            'telefone', 
        ]
        # template_name = 'setorform.html'
        # success_url = reverse_lazy('setorlist')
    
    
