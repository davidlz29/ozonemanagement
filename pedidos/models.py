from django.db import models
from django_extensions.db.models import TimeStampedModel
from articulos.models import Articulo
import django.utils.timezone
from datetime import datetime
from django import forms


class Pedido(TimeStampedModel):

#DATOS SOBRE PEDIDOS
    numero_pedido = models.CharField(max_length=255, null=True)
    fecha = models.DateField(default=django.utils.timezone.now, editable=True)
    lote = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True, verbose_name="Descripción")
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    articulos = models.ForeignKey(Articulo, db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField(blank=True, default=0)
    cliente = models.ForeignKey("clientes.Cliente", db_index=True, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (self.numero_pedido)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-created']


