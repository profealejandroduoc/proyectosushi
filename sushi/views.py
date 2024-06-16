from django.http import Http404
from django.shortcuts import redirect, render
from .forms import ProductoForm, customUserCreationForm
from .models import	Producto
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request, 'sushi/index.html')

def mispedidos(request):
    return render(request, 'sushi/mispedidos.html')

def productos(request):
    
    
    productos=Producto.objects.all()
    page=request.GET.get('page',1)
    
    try:
        pagtr=Paginator(productos,3)
        productos=pagtr.page(page)
    except:
        raise Http404
    
    print(productos)
    datos={
        "productos":productos,
        "paginator":pagtr
    }
    
    if request.method=="POST":
        val=request.POST.get("valor")
        productos=Producto.objects.filter(valor=val)
        
        datos={
        "productos":productos,
      
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
            messages.set_level(request,messages.SUCCESS)
            messages.success(request,'Producto actualizado exitosamente!!')
            return redirect(to='productos')
    
 
    return render(request,'sushi/modificarproducto.html',datos)

def eliminarproducto(request,id):
    producto=get_object_or_404(Producto,id=id)
    
    datos={
        "producto":producto
    }
    
    if request.method=="POST":
        import os
        os.remove(os.path.join(str(settings.MEDIA_ROOT).replace('/media','')+str(producto.imagen.url).replace('/','\\')))
        producto.delete()
        messages.set_level(request, messages.WARNING)
        messages.warning(request,"El producto fue eliminado correctamente!!")
        return redirect(to='productos')
    
    return render(request,'sushi/eliminarproducto.html', datos)

def logout_view(request):
    logout(request) #from django.contrib.auth import logout
    messages.set_level(request,messages.INFO)
    messages.info(request,"Sesión Terminada!!!")
    return redirect(to='index')

def registro(request):
    datos={
        "form":customUserCreationForm()
    }
    
    if request.method=="POST":
        form=customUserCreationForm(data=request.POST)
        newusr=request.POST.get('username')

        existe=User.objects.filter(username=newusr)
        print(existe)
        if len(existe)==0:
            if form.is_valid():
                
                form.save()
                usuario=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
                login(request, usuario)
                messages.success(request,"Usuario creado exitosamente")
                return redirect(to="index")
        else:
            
            datos={
                "form":customUserCreationForm(),
                "alerta": 'Usuario Existente'
            }
                
                
    return render(request,'registration/registro.html', datos)