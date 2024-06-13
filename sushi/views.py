from django.shortcuts import redirect, render
from .forms import ProductoForm
from .models import	Producto
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'sushi/index.html')

def mispedidos(request):
    return render(request, 'sushi/mispedidos.html')

def productos(request):
    productos=Producto.objects.all()
    print(productos)
    datos={
        "productos":productos
    }
    
    return render(request,'sushi/productos.html', datos)

def crearproducto(request):
    form=ProductoForm()
    datos={
        'form':form
    }
    
    if request.method=='POST':
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            datos["mensaje"]='Producto Agregado'
            messages.success(request,'Producto agregado exitosamente!!')
            return redirect('productos')
        else:
            datos["form"]=form
            
    return render(request,'sushi/crearproducto.html',datos)

def modificarproducto(request,id):
    prod=get_object_or_404(Producto, id=id)
    form=ProductoForm(instance=prod)
    
    datos={
        "form":form
    }
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            messages.success('prodcuto actualizado exitosamente!!')
            return redirect(to='productos')
    
 
    return render(request,'sushi/modificarproducto.html',datos)

def eliminarproducto(request,id):
    producto=get_object_or_404(Producto,id=id)
    
    datos={
        "producto":producto
    }
    
    if request.method=="POST":
        producto.delete()
        messages.success(request,"El producto fue eliminado correctamente!!")
        return redirect(to='productos')
    
    return render(request,'sushi/eliminarproducto.html', datos)