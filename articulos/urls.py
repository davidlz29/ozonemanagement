from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ListadoArticulos, DetalleArticulo, ModificarArticulo, NuevoArticulo, EliminarArticulo
from .views import ListadoCategorias, DetalleCategoria, ModificarCategoria, NuevaCategoria,EliminarCategoria

app_name = 'articulos'

urlpatterns = [
    url(r'^listado_articulos/$', ListadoArticulos.as_view(), name="listado_articulos"),
    url(r'^detalle/(?P<pk>.+)/$', DetalleArticulo.as_view(), name="detalle_articulo"),
    url(r'^modificar/(?P<pk>.+)/$', ModificarArticulo.as_view(), name="modificar_articulo"),
    url(r'^nuevo_articulo/', NuevoArticulo.as_view(), name="nuevo_articulo"),
    url(r'^articulo/(?P<pk>[0-9]+)/delete/$', EliminarArticulo.as_view(), name="articulo_eliminar"),

    url(r'^listado_categorias/$', ListadoCategorias.as_view(), name="listado_categorias"),
    url(r'^detalle_categoria/(?P<pk>.+)/$', DetalleCategoria.as_view(), name="detalle_categoria"),
    url(r'^modificar_categoria/(?P<pk>.+)/$', ModificarCategoria.as_view(), name="modificar_categoria"),
    url(r'^nueva_categoria /', NuevaCategoria.as_view(), name="nueva_categoria"),
    url(r'^categoria/(?P<pk>[0-9]+)/delete/$', EliminarCategoria.as_view(), name="categoria_eliminar"),





]


