from django.urls import path
from .views import doc_new
from .views import doc_list
from .views import doc_update
from .views import doc_delete




urlpatterns = [
    path('new/', doc_new, name='doc_new'), 
    path('list/', doc_list, name='doc_list'),
    path('update/<int:id>', doc_update, name='doc_update'),
    path('delete/<int:id>', doc_delete, name='doc_delete'),

]
