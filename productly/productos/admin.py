from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','stock','categoria','creado_en')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)