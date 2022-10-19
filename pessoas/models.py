from enum import unique
from django.db import models
from django.contrib.auth.models import User #importart para utilizar user para validar



# Create your models here.


# def calculateAge(nascimento): 
#     hoje = date.today() 
#     idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day)) 
  
#     return idade

class PessoaModel(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=True, verbose_name='Nome', help_text='Campo Obrigatório')
    genero = models.CharField(max_length=16, blank=False, null=True, verbose_name='Genero', 
            choices=(
                ('MASCULINO',  'MASCULINO'),
                ('FEMININO',  'FEMININO'),
                ('NÃO DEFINIDO', 'NÃO DEFINIDO'),                             
            ))
    nascimento = models.DateTimeField(max_length=9, blank=False, null=True, verbose_name='Nascimento')
    idade = models.IntegerField()
    estadocivil = models.CharField(max_length=15, blank=False, null=True, verbose_name='Estadocivil', 
    choices=(              
            ('S', u'Solteiro'),
            ('C', u'Casado'),
            ('D', u'Divorciado'),
            ('V', u'Viúvo'),
          ))
    escolaridade = models.CharField(max_length=15, blank=False, null=True, verbose_name='Escolaridade',  
        choices=(              
            ('N', u'Nenhum'),
            ('F', u'Ensino Fundamental'),
            ('M', u'Ensino Médio'),
            ('S', u'Ensino Superior'),
          ))
    telefone = models.CharField(max_length=15, blank=False, null=True, unique=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, blank=False, null=True, verbose_name='Email')
    status =models.CharField(max_length=10, blank=False, null=True, verbose_name='Status', 
        choices=(
         ( 'ATIVO' ,  'ATIVO' ),
         ( 'INATIVO' ,  'INATIVO' ),
        ))
    estado = models.CharField(max_length=20, blank=False, null=True, verbose_name='Estado')
    cidade = models.CharField(max_length=20, blank=False, null=True, verbose_name='Cidade')
    criadopor = models.ForeignKey(User, on_delete=models.PROTECT)

    
        
        
        
    def __str__(self):
            return '{} - ({}) - Criado por:({}) '.format(self.nome, self.nascimento, self.criadopor)