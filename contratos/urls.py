from django.urls import path
from .views import ContratoLista, ContratoNew, ContratoDelete, ContratoUpdate




urlpatterns = [
    path('list/', ContratoLista.as_view(), name='contrato_list'),
    path('new/', ContratoNew.as_view(), name='contrato_new'),
    path('update/<int:pk>', ContratoUpdate.as_view(), name='contrato_update'),
    path('delete/<int:pk>', ContratoDelete.as_view(), name='contrato_delete'),

]
