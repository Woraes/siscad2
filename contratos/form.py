from django.forms import ModelForm
from .models import Contrato


class ContratoForm(ModelForm):
    class Meta:
        model = Contrato
        fields = [
            'colaborador',
            'contrato',
            'matricula',
            'setor',
            'unidade',
            'datainicio',
        ]