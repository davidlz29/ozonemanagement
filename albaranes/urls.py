from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ListadoAlbaranes,ModificarAlbaran,NuevoAlbaran,EliminarAlbaran
from . import views

app_name = 'albaranes'

urlpatterns = [

    url(r'^listado_albaranes/$', ListadoAlbaranes.as_view(), name="listado_albaranes"),
    url(r'^detalle_albaran/(?P<pk>.+)/$', views.DetalleAlbaran, name="detalle_albaran"),
    url(r'^modificar_albaran/(?P<pk>.+)/$', ModificarAlbaran.as_view(), name="modificar_albaran"),
    url(r'^nuevo_albaran/', NuevoAlbaran.as_view(), name="nuevo_albaran"),
    url(r'^albaran/(?P<pk>[0-9]+)/delete/$', EliminarAlbaran.as_view(), name="albaran_eliminar"),


]


