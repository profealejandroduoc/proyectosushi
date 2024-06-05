from django import forms
from .models import Producto



class ProductoForm(forms.ModelForm):
    nombre_producto=forms.CharField(widget=forms.TextInput(),help_text='Ingrese nombre del producto')
    descripcion=forms.CharField(widget=forms.TextInput())
    valor=forms.IntegerField(min_value=1000, max_value=10000)
    imagen=forms.ImageField()
                                    
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'valor', 'imagen']
