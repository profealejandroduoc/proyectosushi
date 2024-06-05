
from django.urls import path, include
from .views import index, mispedidos, productos, crearproducto

#IMAGEN
from django.conf import settings
from django.conf.urls.static import static

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('mispedidos/', mispedidos, name='mispedidos'),
    path('productos/', productos, name='productos'),
    path('crearproducto/',crearproducto, name='crearproducto')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)