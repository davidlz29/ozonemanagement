from django.db import models
from django_extensions.db.models import TimeStampedModel
import django.utils.timezone
from datetime import datetime
from django import forms


class Albaran(TimeStampedModel):

#DATOS SOBRE ALBARANES

    cod_albaran = models.CharField(max_length=30, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(default=django.utils.timezone.now, editable=True)

    #Cliente

    cliente = models.ForeignKey("clientes.Cliente", db_index=True, on_delete=models.CASCADE, null=True, blank=True)


   #Profesional

    profesional = models.ForeignKey("profesionales.profesional", db_index=True, on_delete=models.CASCADE, null=True, blank=True)

    #Pedido

    pedido = models.ForeignKey("pedidos.Pedido", db_index=True, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return  (self.cod_albaran)

    class Meta:
        verbose_name = "Albaran"
        verbose_name_plural = "Albaranes"
        ordering = ['-created']


