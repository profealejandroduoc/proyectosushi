from django.forms import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['id','nombre_producto', 'descripcion', 'valor', 'imagen']
'