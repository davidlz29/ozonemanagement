from django.db import models
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
import django.utils.timezone


#(Arrays)

ADMINISTRACION = 1
ALMACEN = 2
MANTENIMIENTO = 3
TRANSPORTE = 4
DIRECCION = 5
CONTABLE = 6

PERFIL = (
    (ADMINISTRACION, 'Administración'),
    (ALMACEN, 'Almacen'),
    (MANTENIMIENTO, 'Mantenimiento'),
    (TRANSPORTE, 'Transporte'),
    (DIRECCION, 'Direccion'),
    (CONTABLE, 'Contable'),
)

NIF = 1
NIE = 2
PASAPORTE = 3

TIPODOCUMENTO = (
    (NIF, 'Nif'),
    (NIE, 'Nie'),
    (PASAPORTE, 'Pasaporte'),
)

HOMBRE=1
MUJER=2

SEXO = (
    (HOMBRE, 'Hombre'),
    (MUJER, 'Mujer'),
)


CASADO = 1
SOLTERO = 2
VIUDO = 3
DIVORCIADO = 4

ESTADOCIVIL = (
    (CASADO, 'Casado'),
    (SOLTERO, 'Soltero'),
    (VIUDO, 'Viudo'),
    (DIVORCIADO, 'Divorciado'),
)

#Tipos de contrato

TEMP3 = 1
TEMP6 = 2
TEMP9 = 3
TEMP12 = 4
INDEFINIDO = 5
PRACTICAS = 6


TIPOCONTRATO=(
    (TEMP3, 'Temporal 3 Meses'),
    (TEMP6, 'Temporal 6 Meses'),
    (TEMP9, 'Temporal 9 Meses'),
    (TEMP12, 'Temporal 12 Meses'),
    (INDEFINIDO, 'Indefinido'),
    (PRACTICAS, 'En prácticas'),
)

#Modelos

class Profesional(TimeStampedModel):

# DATOS SOBRE LOS PROFESIONALES
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    tipo_documento = models.IntegerField(default=NIF, choices=TIPODOCUMENTO, db_index=True, null=True, blank=True)
    num_documento = models.CharField(max_length=9, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    sexo = models.IntegerField(choices=SEXO, default=HOMBRE, db_index=True, null=True, blank=True)
    estado_civil = models.IntegerField(choices=ESTADOCIVIL, default=SOLTERO, blank=True, null=True)
    hijos = models.PositiveIntegerField(default=0, blank=True, null=True)
    perfil = models.IntegerField(default=ALMACEN, choices=PERFIL, db_index=True, null=True, blank=True)
    dir_calle = models.CharField(null=True, max_length=255, blank=True, verbose_name="Calle")
    dir_num = models.CharField(null=True, max_length=255, blank=True, verbose_name="Número")
    dir_piso = models.CharField(null=True, max_length=255, blank=True, verbose_name="Piso/Planta")
    codigo_postal = models.CharField(null=True, blank=True, max_length=15)
    provincias = models.ForeignKey("clientes.Provincias", db_index=True, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name="Provincia")
    poblacion = models.ForeignKey("clientes.Poblacion", db_index=True, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name="Población")
    telefono = models.CharField(max_length=20, null=True, blank=True)
    movil = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(blank=True)
    tipo_contrato = models.IntegerField(choices=TIPOCONTRATO, default=TEMP3, db_index=True, null=True, blank=True,
                                        verbose_name="Tipo de Contrato")
    fecha_vencimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de Vencimiento")
    fecha_alta = models.DateField(blank=True, null=True, verbose_name="Fecha de Alta")
    iban = models.CharField(max_length=24, null=True, blank=True, verbose_name="IBAN")

#Funciones para devolver un tipo String

    def __str__(self):
        return "{} - {}".format(self.nombre, self.apellidos)

    def tipo_contrato_display(self):
        return '%s' % (self.get_tipo_contrato_display())

    def tipo_documento_display(self):
        return '%s' % (self.get_tipo_documento_display())


    def perfil_display(self):
        return '%s' % (self.get_perfil_display())

    def sexo_display(self):
        return '%s' % (self.get_sexo_display())

    def estado_civil_display(self):
        return '%s' % (self.get_estado_civil_display())

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['-created']



class TipoDocumentos(TimeStampedModel):
    code = models.PositiveIntegerField()
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "tipo documento"
        verbose_name_plural = "tipo documentos"
        ordering = ['-created']


class Documentos(TimeStampedModel):
    profesional = models.ForeignKey("Profesional", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    tipodocumento = models.ForeignKey("TipoDocumentos", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    etiqueta = models.CharField(max_length=255)
    fecha_documento = models.DateField(default= django.utils.timezone.now, editable=True)
    documento = models.FileField(upload_to='documentos', null=True, blank=True)

    def __str__(self):
        return self.etiqueta

    def extension(self):
        name, extension = os.path.splitext(self.documento.name)
        return extension

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ['-created']



class Bajas(TimeStampedModel):
    profesional = models.ForeignKey("Profesional", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    etiqueta = models.CharField(max_length=255)
    fecha_documento = models.DateField(default= django.utils.timezone.now, editable=True)
    bajas = models.FileField(upload_to='bajas_profesionales', null=True, blank=True)

    def __str__(self):
        return self.etiqueta

    def extension(self):
        name, extension = os.path.splitext(self.bajas.name)
        return extension

    class Meta:
        verbose_name = "baja"
        verbose_name_plural = "bajas"
        ordering = ['-created']

