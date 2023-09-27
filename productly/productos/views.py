from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import Form

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
    #try:
        producto = get_object_or_404(Producto,id=producto_id)
        #producto = Producto.objects.get(id=producto_id)
        return render(request,
                    'detalle.html',
                    context={ 'producto': producto })
    #except Producto.DoesNotExist:
        #raise Http404()

def formulario(request):
    form = Form()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )