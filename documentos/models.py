from colaboradores.models import Colaborador
from django.db import models

# Create your models here.


def userdoc(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'User\{0}'.format(instance)

class Documento(models.Model):
        nome = models.ForeignKey(Colaborador, on_delete=models.PROTECT, null=True, verbose_name="Colaborador")
        data = models.DateField(null=True, blank=False)
        tipo = models.CharField(max_length=10, choices=(
            ('Documento', 'Documento'),
            ('Atestado', 'Atestado'),
            ('Foto', 'Foto'),
            ('PDF', 'PDF'),
        ))
        anexo = models.ImageField(upload_to=userdoc, null=True, blank=False, verbose_name="Anexo")
        obs = models.TextField(null=True, blank=False, verbose_name="Observação")
        
        def __str__(self):
            return '{} - Data:({}) '.format(self.nome, self.data)
 