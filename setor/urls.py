from django.urls import path
from .views import setor_new
from .views import setor_list
from .views import setor_update
from .views import setor_delete




urlpatterns = [
    path('new/', setor_new, name='setor_new'), 
    path('list/', setor_list, name='setor_list'),
    path('update/<int:id>', setor_update, name='setor_update'),
    path('delete/<int:id>', setor_delete, name='setor_delete'),
]
