from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ListadoProveedores, DetalleProveedor, ModificarProveedor, NuevoProveedor, EliminarProveedor
from .views import ListadoGastos, DetalleGasto, ModificarGasto, NuevoGasto, EliminarGasto

app_name = 'gastos'

urlpatterns = [

    url(r'^listado_proveedores/$', ListadoProveedores.as_view(), name="listado_proveedores"),
    url(r'^detalle_proveedor/(?P<pk>.+)/$', DetalleProveedor.as_view(), name="detalle_proveedor"),
    url(r'^modificar_proveedor/(?P<pk>.+)/$', ModificarProveedor.as_view(), name="modificar_proveedor"),
    url(r'^nuevo_proveedor/', NuevoProveedor.as_view(), name="nuevo_proveedor"),
    url(r'^proveedor/(?P<pk>[0-9]+)/delete/$', EliminarProveedor.as_view(), name="proveedor_eliminar"),

    url(r'^listado_gastos/$', ListadoGastos.as_view(), name="listado_gastos"),
    url(r'^detalle_gasto/(?P<pk>.+)/$', DetalleGasto.as_view(), name="detalle_gasto"),
    url(r'^modificar_gasto/(?P<pk>.+)/$', ModificarGasto.as_view(), name="modificar_gasto"),
    url(r'^nuevo_gasto/', NuevoGasto.as_view(), name="nuevo_gasto"),
    url(r'^gasto/(?P<pk>[0-9]+)/delete/$', EliminarGasto.as_view(), name="gasto_eliminar"),
]

