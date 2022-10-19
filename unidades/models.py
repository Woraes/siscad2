from django.db import models
from django.core.validators import RegexValidator
#para importar um app
from setor.models import Setor



class Unidade(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=True, verbose_name='Nome da Unidade')
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, verbose_name='Setor')
    ramal = models.IntegerField(blank=True, null=True, verbose_name='Ramal')
    status =models.CharField(max_length=10, blank=False, null=True, verbose_name='Status', 
        choices=(
         ( 'ATIVO' ,  'ATIVO' ),
         ( 'INATIVO' ,  'INATIVO' ),
        ))    
    descricao = models.CharField(max_length=70, blank=True, null=True, verbose_name='Descricao')
    
    
    
    def __str__(self):
        return '{} ({}) {}'.format(self.nome, self.setor.sigla, self.setor.nome)


