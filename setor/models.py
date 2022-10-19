from django.db import models
from django.core.validators import RegexValidator


class Setor(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=True, verbose_name='Nome do setor')
    sigla = models.CharField(max_length=7, blank=False, null=True, verbose_name='Sigla do Setor')
    descricao = models.CharField(max_length=70, blank=True, null=True, verbose_name='Descrição do Setor')
    estado = models.CharField(max_length=2, verbose_name='UF')
    cidade = models.CharField(max_length=25, blank=False, null=True, verbose_name='Cidade')
    municipio = models.CharField(max_length=25, blank=False, null=True, verbose_name='Municipio')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telefone = models.CharField(validators = [phoneNumberRegex],max_length=17, blank=False, null=True, verbose_name='Telefone', )
    

    
    
    def __str__(self):
        return '{} ({})'.format(self.sigla, self.nome)