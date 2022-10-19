from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome = models.CharField(max_length=55, blank=False, null=True, verbose_name='Nome')
    cpf = models.CharField(max_length=14, blank=False, null=True, verbose_name='Cpf')
    telefone = models.CharField(max_length=20, blank=False, null=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, blank=False, null=True, verbose_name='Email')
    cep = models.CharField(max_length=20, blank=False, null=True, verbose_name='Cep')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Usuario')
    
    def __str__(self):
         return 'Nome: ({}) - Criado por:({}) '.format(self.nome,self.usuario)     
