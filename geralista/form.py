from django.forms import ModelForm
from .models import Geralista


class GeralistaForm(ModelForm):
    class Meta:
        model = Geralista
        fields = ['menssagem',
              'arquivo1',
              'arquivo2',
              'arquivo3',
        
    ]