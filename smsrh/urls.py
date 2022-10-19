"""smsrh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#acresento o include para poder chamar as urls dos apps
from django.urls import path, include
#from nomeapp import urls as nomeapp_urls
from pages import urls as pages_urls
from setor import urls as setor_urls
from colaboradores import urls as colaborador_urls
from unidades import urls as unidades_urls

from pessoas import urls as pessoas_urls
from contratos import urls as contratos_urls
from usuarios import urls as usuarios_urls
from geralista import urls as geralista_urls

#para ver os upload no modo dessenvolvimento
from django.conf import settings
from django.conf.urls.static import static


#importa todas as urls criadas nos apps da páginas
urlpatterns = [
    path('admin/', admin.site.urls),
    #path ('endereço do navegador/', include(nomeapp_urls)),
    path ('', include(pages_urls)),
    path ('unidade/', include(unidades_urls)),
    path ('setor/', include(setor_urls)),
    path ('colaborador/', include(colaborador_urls)),
    
    path('pessoas/', include(pessoas_urls)),
    path('contrato/',include(contratos_urls)),
    path('', include(usuarios_urls)),
    path('', include(geralista_urls)),
]


# montando a condição para ver arquivis upload no modo dessenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
