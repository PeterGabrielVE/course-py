from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    #productos = Producto.objects.all().values()
    #productos = Producto.objects.filter(puntaje=3)
    #productos = Producto.objects.get(pk=1)
    #return HttpResponse('hola mundo')
    #return JsonResponse(list(productos), safe=False)
    return render(request,'index.html',
    context={'productos':productos})


def detalle(request, producto_id):
    #return HttpResponse(producto_id)
    producto = Producto.objects.get(id=producto_id)
    return render(request,
                'detalle.html',
                context={ 'producto': producto })