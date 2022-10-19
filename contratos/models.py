from django.db import models
from django.db import models
from django.core.validators import RegexValidator
from setor.models import Setor #importar appmodels
from unidades.models import Unidade
from colaboradores.models import Colaborador
from django.contrib.auth.models import User #importart para utilizar user para validar



class Contrato(models.Model):
        colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT, verbose_name='Colaborador')
        contrato = models.CharField(max_length=30, blank=False, null=True, unique=True, verbose_name='Número Contrato')
        matricula = models.IntegerField(blank=False, unique=True, verbose_name='Matrícula')
        setor = models.ForeignKey(Setor, on_delete=models.PROTECT,  verbose_name='Setor')
        unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, verbose_name='Unidade')
        datainicio = models.DateField(verbose_name='Data Início', blank=False)
        criadopor = models.ForeignKey(User, on_delete=models.PROTECT)
    
        def __str__(self):
            return '{} - ({}) - Criado por:({}) '.format(self.colaborador, self.matricula, self.criadopor)