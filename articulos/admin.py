from django.contrib import admin
from .models import Categoria, Articulo, ArticuloPedido


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(ArticuloPedido)