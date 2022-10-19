from enum import unique
from django.db import models
from django.contrib.auth.models import User



class Geralista(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=True, verbose_name='titulo')
    menssagem = models.TextField(max_length=1000, blank=False, null=True, verbose_name='Menssagem')
    arquivo1 = models.FileField(upload_to='arquivo1/',blank=True, verbose_name='arquivo1')
    arquivo2 = models.FileField(upload_to='arquivo2/',blank=True, verbose_name='arquivo2')
    arquivo3 = models.FileField(upload_to='arquivo3/',blank=True, verbose_name='arquivo3')
    criadopor = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
         return 'Menssagem: ({}) - Criado por:({}) '.format(self.menssagem,self.criadopor)     
