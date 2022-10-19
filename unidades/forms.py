from django.forms import ModelForm, Form
from django.db import models
from.models import Unidade


    
    
class Unidadeform(ModelForm):
    class Meta:
        model = Unidade
        fields = [
            'nome', 
            'setor', 
            'ramal',
            'status',
            'descricao',
        
            ]    
    