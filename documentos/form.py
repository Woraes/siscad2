from django.forms import ModelForm
from.models import Documento


class Documentoform(ModelForm):
    class Meta:
        model = Documento
        fields =  [
            'nome',
            'data',
            'tipo',
            'obs',
            
        ]