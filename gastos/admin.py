from django.contrib import admin
from .models import Gasto, Proveedor, GrupoGasto

#Register your models here.

admin.site.register(GrupoGasto)
admin.site.register(Proveedor)
admin.site.register(Gasto)