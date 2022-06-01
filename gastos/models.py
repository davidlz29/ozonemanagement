import os
from django.db import models
from django_extensions.db.models import TimeStampedModel
from datetime import datetime
import django.utils.timezone
from django import forms


NIF = 1
NIE = 2
CIF = 3

TIPODOCUMENTO = (
    (NIF, 'Nif'),
    (NIE, 'Nie'),
    (CIF, 'Cif'),
)

FACTURA = 1
TICKET = 2

TIPODOCUMENTO_GASTO = (
    (FACTURA, 'Factura'),
    (TICKET, 'Ticket'),
)

TARJETA = 1
TRANSFERENCIA = 2
EFECTIVO = 3
INGRESO = 4

FORMAPAGO = (
    (TARJETA, 'Tarjeta de Credito'),
    (TRANSFERENCIA, 'Transferencia Bancaria'),
    (EFECTIVO, 'Efectivo'),
    (INGRESO, 'Ingreso Bancario'),
)


GENERAL = 1
REDUCIDO = 2
SUPER = 3

IVA = (
    (GENERAL, 'Iva General (21%)'),
    (REDUCIDO, 'Iva Reducido (10%)'),
    (SUPER, 'Iva Superreducido (4%)'),
)


class GrupoGasto(TimeStampedModel):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Grupo de gasto"
        verbose_name_plural = "Grupos de Gastos"
        ordering = ['-created']

class Proveedor(TimeStampedModel):

#DATOS SOBRE PROVEEDORES
    razon_social = models.CharField(max_length=255, null=True)
    tipo_documento = models.IntegerField(default=CIF, choices=TIPODOCUMENTO, db_index=True, null=True)
    num_documento = models.CharField(max_length=30, null=True)
    fecha_alta = models.DateField(default=django.utils.timezone.now, null=True)
    dir_calle = models.CharField(max_length=255, verbose_name="calle", null=True)
    dir_numero = models.CharField(max_length=25, verbose_name="numero" ,null=True, blank=True)
    dir_piso_puerta = models.CharField(max_length=255, verbose_name="piso puerta", null=True, blank=True )
    cod_postal = models.IntegerField(null=True)
    provincias = models.ForeignKey("clientes.Provincias", db_index=True, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Provincia")
    poblacion = models.ForeignKey("clientes.Poblacion", db_index=True, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Población")


    def tipo_documento_display(self):
        return '%s' % (self.get_tipo_documento_display())


    def __str__(self):
        return "{} {}".format(self.razon_social, self.num_documento)



    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['-created']

class Gasto(TimeStampedModel):
#DATOS SOBRE GASTOS
    nombre = models.CharField(max_length=255)
    fecha = models.DateField(default=django.utils.timezone.now, editable=True, null=True, blank=True)
    Descripcion = models.CharField(max_length=255, blank=True, null=True)
    num_factura = models.CharField(max_length=255, blank=True, null=True)
    tipo_doc = models.IntegerField(default=TICKET, choices=TIPODOCUMENTO_GASTO, db_index=True, null=True, blank=True)
    proveedor = models.ForeignKey("Proveedor", db_index=True, on_delete=models.CASCADE)
    iva = models.IntegerField(default=GENERAL, choices=IVA, db_index=True, null=True, blank=True)
    forma_pago = models.IntegerField(default=EFECTIVO, choices=FORMAPAGO, db_index=True, null=True, blank=True)
    almacenable = models.BooleanField(default=False)
    unidades = models.PositiveIntegerField(blank=True, null=True)
    fecha_caducidad = models.DateField(default=django.utils.timezone.now, editable=True, null=True, blank=True)
    documento = models.FileField(upload_to='documentos_gastos', null=True, blank=True)

    def tipo_doc_display(self):
        return '%s' % (self.get_tipo_doc_display())


    def forma_pago_display(self):
        return '%s' % (self.get_forma_pago_display())

    def iva_display(self):
        return '%s' % (self.get_iva_display())


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
        ordering = ['-created']