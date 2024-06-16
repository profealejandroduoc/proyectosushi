
from django.urls import path, include
from .views import index, mispedidos, productos, crearproducto, modificarproducto, eliminarproducto,logout_view,\
    registro
    

#IMAGEN
from django.conf import settings
from django.conf.urls.static import static

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('mispedidos/', mispedidos, name='mispedidos'),
    path('productos/', productos, name='productos'),
    path('crearproducto/',crearproducto, name='crearproducto'),
    path('modificarproducto/<id>',modificarproducto, name='modificarproducto'),
    path('eliminarproducto/<id>',eliminarproducto,name='eliminarproducto'),
    path('logout_view/',logout_view,name='logout_view'),
    path('registro',registro,name='registro')
    
 
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)