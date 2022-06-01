from django.conf.urls import url
from django.conf import settings
from .views import ListadoClientes, ModificarCliente, DetalleCliente , NuevoCliente , EliminarCliente,ModificarDocumento,EliminarDocumento
from .views import  DocumentosNuevo, FotoNueva, ModificarFoto, EliminarFoto
from . import views
from django.conf.urls.static import static

app_name = 'clientes'

urlpatterns = [

    url(r'^listado_clientes/$', ListadoClientes.as_view(), name="listado_clientes"),
    url(r'^detalle_cliente/(?P<pk>.+)/$', DetalleCliente.as_view(), name="detalle_cliente"),
    url(r'^modificar_cliente/(?P<pk>.+)/$', ModificarCliente.as_view(), name="modificar_cliente"),
    url(r'^nuevo_cliente/', NuevoCliente.as_view(), name="nuevo_cliente"),
    url(r'^cliente/(?P<pk>[0-9]+)/delete/$', EliminarCliente.as_view(), name="cliente_eliminar"),


    url(r'^documentos_cliente/(?P<pk>[0-9-]+)/$', views.documentos_cliente, name="documentos_cliente"),
    url(r'^documentos_nuevo/(?P<client>[0-9]+)/$', DocumentosNuevo.as_view(), name="documentos_nuevo"),
    url(r'^documento_modificar/(?P<pk>[0-9]+)/$', ModificarDocumento.as_view(), name="documento_modificar"),
    url(r'^documento/(?P<pk>[0-9]+)/delete/$', EliminarDocumento.as_view(), name="documento_eliminar"),

    url(r'^fotos_cliente/(?P<pk>[0-9-]+)/$', views.fotos_cliente, name="fotos_cliente"),
    url(r'^foto_nueva/(?P<client>[0-9]+)/$', FotoNueva.as_view(), name="foto_nueva"),
    url(r'^foto_modificar/(?P<pk>[0-9]+)/$', ModificarFoto.as_view(), name="foto_modificar"),
    url(r'^foto/(?P<pk>[0-9]+)/delete/$', EliminarFoto.as_view(), name="foto_eliminar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


