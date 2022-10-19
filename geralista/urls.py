from django.urls import path
from django.contrib.auth import views as auth_views
from .views import GeraListaNew,GeraListaList, Waths ,AcompanhaExe, GeraListaUpdate, GeralistaDelete,exportar_xlsx,juntartabelas





urlpatterns = [
    path('list/', GeraListaList.as_view(), name='geralista_list'),
    path('new/', GeraListaNew.as_view(), name='geralista_new'),
    path('update/<int:pk>', GeraListaUpdate.as_view(), name='geralista_update'),
    path('delete/<int:pk>', GeralistaDelete.as_view(), name='geralista_delete'),
    path('execut/', Waths , name='execut'),
    path('export/', exportar_xlsx , name='export'),
    path('export/', juntartabelas , name='juntar'),
    path('painelexe/', AcompanhaExe.as_view(), name='painelexe'),

]
