from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ListadoPedidos, NuevoPedido, EliminarPedido,ModificarPedido
from . import views

app_name = 'pedidos'
urlpatterns = [

    url(r'^listado_pedidos/$', ListadoPedidos.as_view(), name="listado_pedidos"),
    url(r'^nuevo_pedido/', NuevoPedido.as_view(), name="nuevo_pedido"),
    url(r'^modificar_pedido/(?P<pk>.+)/$', ModificarPedido.as_view(), name="modificar_pedido"),
    url(r'^pedido/(?P<pk>[0-9]+)/delete/$', EliminarPedido.as_view(), name="pedido_eliminar"),
    url(r'^addarticulo_pedido/(?P<pk>.+)/$', views.AddArticuloPedido, name="addarticulo_pedido"),
    url(r'^detalle_pedido/(?P<pk>.+)/$', views.DetalleArticuloPedido, name="detalle_pedido"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
