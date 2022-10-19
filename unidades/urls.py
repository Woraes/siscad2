from django.urls import path

#importar as views que foi criada de views.py
#from .views import Setorcreate, Unidadecreate
from .views import unidade_new






#apos criar as urls sempre declaras elas na central de urls.py
#importar as views que foi criada de views.py
#from .views import Setorcreate, Unidadecreate
from .views import unidade_list, unidade_new, unidade_update,unidade_delete


#padroa django urlpatterns
urlpatterns = [
   #path('endereço do navegador', minhaView.as_view(), name='nome da url')
#    path('create/setor/', Setorcreate.as_view(), name='create-setor'),
#    path('create/unidade/', Unidadecreate.as_view(), name='create-unidade'),
     path('new/', unidade_new, name='unidade_new'),
     path('list/', unidade_list, name='unidade_list'),
     path('update/<int:id>', unidade_update, name='unidade_update'),
     path('delete/<int:id>', unidade_delete, name='unidade_delete'),
      
]
