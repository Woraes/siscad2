from django.contrib import admin
from .models import PessoaModel
from django.contrib.admin.filters import SimpleListFilter

admin.site.register(PessoaModel)

