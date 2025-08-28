# classificador/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    # Quando a URL for vazia (''), execute a view 'index'
    path('', views.index, name='index'), 
]