
from django.urls import path, include

from .views import index, mispedidos

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('mispedidos', mispedidos, name='mispedidos')
]
