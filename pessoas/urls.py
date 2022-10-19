from django.urls import path
from .views import PessoaList, PessoaNew, PessoaUpdate, PessoaDelete





urlpatterns = [
    path('list/', PessoaList.as_view(), name='pessoa_list'),
    path('new/', PessoaNew.as_view(), name='pessoa_new'),
    path('update/<int:pk>', PessoaUpdate.as_view(), name='pessoa_update'),
    path('delete/<int:pk>', PessoaDelete.as_view(), name='pessoa_delete'),
]
