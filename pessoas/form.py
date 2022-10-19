from django.forms import ModelForm
from .models import PessoaModel


class Pessoaform(ModelForm):
    class Meta:
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