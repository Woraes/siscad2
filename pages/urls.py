from unicodedata import name
from django.urls import path
from .views import  Sobre, Ajuda, Registrar, index



urlpatterns = [
    # path('endereço/', minhaview.as_view(), name='nome da url'),
    # path('', IndexView.as_view(), name='home'),
    # path('', IndexView.as_view(), name='home'),
    path('', index, name='home'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('ajuda/', Ajuda.as_view(), name='ajuda'),
    path('registrar/', Registrar.as_view(), name='registrar'),    
]