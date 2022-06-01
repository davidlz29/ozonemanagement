from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ListadoAlmacen, ModificarAlmacen, DetalleAlmacen, NuevoAlmacen, EliminarAlmacen

app_name = 'almacen'

urlpatterns = [

    url(r'^listado_almacen/$', ListadoAlmacen.as_view(), name="listado_almacen"),
    url(r'^detalle_almacen/(?P<pk>.+)/$', DetalleAlmacen.as_view(), name="detalle_almacen"),
    url(r'^modificar_almacen/(?P<pk>.+)/$', ModificarAlmacen.as_view(), name="modificar_almacen"),
    url(r'^nuevo_almacen/', NuevoAlmacen.as_view(), name="nuevo_almacen"),
    url(r'^almacen/(?P<pk>[0-9]+)/delete/$', EliminarAlmacen.as_view(), name="almacen_eliminar"),


]

