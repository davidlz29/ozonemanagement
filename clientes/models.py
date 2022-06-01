from django.db import models
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
import django.utils.timezone


PROFESIONAL = 1
PARTICULAR = 2

TIPOCLIENTE = (
    (PROFESIONAL, 'Profesional'),
    (PARTICULAR, 'Particular'),
)

NIF = 1
NIE = 2
CIF = 3

TIPODOCUMENTO = (
    (NIF, 'Nif'),
    (NIE, 'Nie'),
    (CIF, 'Cif'),
)



INDEFINIDO = 1
HOMBRE = 2
MUJER = 3

SEXO = (
    (INDEFINIDO, 'Indefinido'),
    (HOMBRE, 'Hombre'),
    (MUJER, 'Mujer'),
)



class Provincias(TimeStampedModel):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    cod_provincia = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "provincia"
        verbose_name_plural = "provincias"
        ordering = ['-created']

class Poblacion(TimeStampedModel):
    nombre = models.CharField(max_length=255)
    cod_poblacion = models.CharField(max_length=255)
    cod_provincia = models.CharField(max_length=255)
    provincias = models.ForeignKey("Provincias", db_index=True, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "poblacion"
        verbose_name_plural = "poblacion"
        ordering = ['-created']


class Cliente(TimeStampedModel):

    #INFORMACION SOBRE EL CLIENTE

    tipo_cliente = models.IntegerField(default=PROFESIONAL, choices=TIPOCLIENTE, db_index=True, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellidos = models.CharField(max_length=255)
    tipo_documento = models.IntegerField(default=CIF, choices=TIPODOCUMENTO, db_index=True, null=True, blank=True)
    num_documento = models.CharField(max_length=9, blank=True, null=True)
    fecha_nacimiento = models.DateField(default=django.utils.timezone.now, editable=True,blank=True, null=True)
    dir_calle = models.CharField(null=True, max_length=255, blank=True, verbose_name="Calle")
    dir_numero = models.CharField(null=True, max_length=255, blank=True, verbose_name="Número")
    dir_piso = models.CharField(null=True, max_length=255, blank=True, verbose_name="Piso/Planta")
    codigo_postal = models.CharField(null=True, blank=True, max_length=8)
    provincias = models.ForeignKey("provincias", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    poblacion = models.ForeignKey("poblacion", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True,verbose_name="Télefono")
    movil = models.CharField(max_length=20, null=True, blank=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    profesion = models.CharField(max_length=50, blank=True, null=True)
    fecha_alta = models.DateField(default=django.utils.timezone.now, editable=True, blank=True, null=True)
    sexo = models.IntegerField(default=INDEFINIDO, choices=SEXO, db_index=True, null=True, blank=True)


    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)

    def tipo_documento_display(self):
        return '%s' % (self.get_tipo_documento_display())

    def num_documento_display(self):
        return '%s' % (self.get_num_documento_display())



    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
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
    cliente = models.ForeignKey("Cliente", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    tipodocumento = models.ForeignKey("TipoDocumentos", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    etiqueta = models.CharField(max_length=255)
    fecha_documento = models.DateField(default= django.utils.timezone.now, editable=True)
    documento = models.FileField(upload_to='documentos_cliente', null=True, blank=True)

    def __str__(self):
        return self.etiqueta

    def extension(self):
        name, extension = os.path.splitext(self.documento.name)
        return extension

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ['-created']


class Fotos(TimeStampedModel):
    cliente = models.ForeignKey("Cliente", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    etiqueta = models.CharField(max_length=255)
    fecha_foto = models.DateField(default= django.utils.timezone.now, editable=True)
    foto = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.etiqueta

    def extension(self):
        name, extension = os.path.splitext(self.imagenes.name)
        return extension



    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "fotos"
        ordering = ['-created']