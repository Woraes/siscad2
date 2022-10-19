from django.forms import ModelForm
from.models import Colaborador






class Colaboradorform(ModelForm):
    class Meta:
        model = Colaborador
        fields = [
            'nome',
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