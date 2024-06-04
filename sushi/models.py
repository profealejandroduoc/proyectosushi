from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto=models.CharField(max_length=50, null=False)
    imagen=models.ImageField(upload_to='productos', null=True)
    descripcion=models.CharField(max_length=50, null=False)
    valor=models.IntegerField(null=False)
    


    def __str__(self):
        return self.nombre_producto