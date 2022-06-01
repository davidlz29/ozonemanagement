from django.db import models
from django_extensions.db.models import TimeStampedModel
from datetime import datetime
from django import forms


class Categoria(TimeStampedModel):

#DATOS SOBRE CATEGORIAS
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

class Articulo(TimeStampedModel):

#DATOS SOBRE ARTICULOS
    categoria = models.ForeignKey(Categoria, db_index=True, on_delete=models.CASCADE)
    proveedor = models.ForeignKey("gastos.Proveedor", db_index=True, on_delete=models.CASCADE)
    codigo = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)



    def __str__(self):

        return "{} {}".format(self.nombre, self.proveedor)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created']



class ArticuloPedido(TimeStampedModel):
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    cod_articulo = models.ForeignKey("articulos.Articulo", null=True, blank=True, db_index=True, on_delete=models.CASCADE)
    cod_pedido = models.ForeignKey("pedidos.Pedido", null=True, blank=True, db_index=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return "{} {}".format(self.cod_articulo, self.cantidad)

    class Meta:
        verbose_name = "ArticuloPedido"
        verbose_name_plural = "ArticulosPedidos"
        ordering = ['-created']