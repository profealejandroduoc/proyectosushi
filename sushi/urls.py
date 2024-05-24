
from django.urls import path, include

from .views import index, mispedidos, productos

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('mispedidos/', mispedidos, name='mispedidos'),
    path('productos/', productos, name='productos'),
]
