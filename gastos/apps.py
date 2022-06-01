from django.contrib import admin
from .models import GrupoGasto, Proveedor, Gasto

admin.site.register(GrupoGasto)
admin.site.register(Proveedor)
admin.site.register(Gasto)