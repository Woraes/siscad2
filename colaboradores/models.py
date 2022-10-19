from enum import unique
from django.db import models
from django.contrib.auth.models import User





class Colaborador(models.Model):
        nome = models.CharField(max_length=60, blank=False, null=True, verbose_name='Nome')
        nascimento = models.DateField(max_length=9, blank=False, null=True, verbose_name='Nascimento')
        estadocivil = models.CharField(max_length=15, blank=False, null=True, verbose_name='Estadocivil', 
          choices=(              
            ('S', u'Solteiro'),
            ('C', u'Casado'),
            ('D', u'Divorciado'),
            ('V', u'Viúvo'),
          ))
        rg = models.CharField(max_length=15, blank=False, null=True, verbose_name='Rg')
        cpf = models.CharField(max_length=15, blank=False, null=True, unique=True, verbose_name='CPF')
        pis = models.CharField(max_length=16, blank=False, null=True, unique=True, verbose_name='PIS')
        cns = models.CharField(max_length=16, blank=False, null=True, unique=True, verbose_name='Cns')
        ctps = models.CharField(max_length=7, blank=False, null=True, verbose_name='Ctps número:')
        ctpsserie = models.CharField(max_length=4, blank=False, null=True, verbose_name='Série')
        ctpsuf = models.CharField(max_length=2, blank=False, null=True, verbose_name='UF')
        
        
        genero = models.CharField(max_length=16, blank=False, null=True, verbose_name='Genero', 
            choices=(
                ('MASCULINO',  'MASCULINO'),
                ('FEMININO',  'FEMININO'),
                ('NÃO DEFINIDO', 'NÃO DEFINIDO'),                             
            ))
        phone = models.CharField(max_length=16, blank=False, null=True, verbose_name='Celular')
        email = models.CharField(max_length=50, blank=True, null=True, verbose_name='Email')
        foto = models.ImageField(upload_to='Colaborador_foto', null=True , blank=True, verbose_name='Foto')
        
        
        status =models.CharField(max_length=10, blank=False, null=True, verbose_name='Status', 
        choices=(
         ( 'ATIVO' ,  'ATIVO' ),
         ( 'INATIVO' ,  'INATIVO' ),
        ))
        criadopor = models.ForeignKey(User, on_delete=models.PROTECT)
        def __str__(self):
            return '{} - ({}) - Criado por:({}) '.format(self.nome, self.cpf, self.criadopor)     
       