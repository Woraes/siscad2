from django.urls import path
from .views import ColaboradorNew
from .views import ColaboradorLista
from .views import ColaboradorUpdate
from .views import ColaboradorDelete




urlpatterns = [
    path('new/', ColaboradorNew.as_view(), name='colaborador_new'), 
    path('list/', ColaboradorLista.as_view(), name='colaborador_list'),
    path('update/<int:pk>', ColaboradorUpdate.as_view(), name='colaborador_update'),
    path('delete/<int:pk>', ColaboradorDelete.as_view(), name='colaborador_delete'),
]