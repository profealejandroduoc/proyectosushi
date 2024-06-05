from django.shortcuts import redirect, render
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'sushi/index.html')

def mispedidos(request):
    return render(request, 'sushi/mispedidos.html')

def productos(request):
    return render(request,'sushi/productos.html')

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
            return redirect('productos')
        else:
            datos["form"]=form
            
    return render(request,'sushi/crearproducto.html',datos)
          