from django.contrib import admin
from .models import Producto


class AdmProducto(admin.ModelAdmin):
    list_display = ['id','nombre_producto', 'descripcion', 'valor', 'imagen']
    search_fields = ['nombre_producto', 'descripcion']
    list_filter = ['valor']
    ordering = ['nombre_producto']
  
    
# Register your models here.
admin.site.register(Producto,AdmProducto)