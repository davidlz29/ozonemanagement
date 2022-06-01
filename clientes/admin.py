from django.contrib import admin
from .models import Cliente, TipoDocumentos

admin.site.register(Cliente)
admin.site.register(TipoDocumentos)