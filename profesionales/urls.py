from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ListadoProfesionales, DetalleProfesional, ModificarProfesional, NuevoProfesional, EliminarProfesional
from .views import DocumentosNuevo,ModificarDocumento,EliminarDocumento, BajasNuevo, EliminarBaja, ModificarBaja
from . import views
from django.conf.urls.static import static

app_name = 'profesionales'

urlpatterns = [

    url(r'^listado_profesionales/$', ListadoProfesionales.as_view(), name="listado_profesionales"),
    url(r'^detalle_profesional/(?P<pk>.+)/$', DetalleProfesional.as_view(), name="detalle_profesional"),
    url(r'^modificar_profesional/(?P<pk>.+)/$', ModificarProfesional.as_view(), name="modificar_profesional"),
    url(r'^nuevo_profesional/', NuevoProfesional.as_view(), name="nuevo_profesional"),
    url(r'^profesional/(?P<pk>[0-9]+)/delete/$', EliminarProfesional.as_view(), name="profesional_eliminar"),

    url(r'^documentos_profesionales/(?P<pk>[0-9-]+)/$', views.documentos_profesionales, name="documentos_profesionales"),
    url(r'^documentos_nuevo/(?P<prof>[0-9]+)/$', DocumentosNuevo.as_view(), name="documentos_nuevo"),
    url(r'^documento_modificar/(?P<pk>[0-9]+)/$', ModificarDocumento.as_view(), name="documento_modificar"),
    url(r'^documento/(?P<pk>[0-9]+)/delete/$', EliminarDocumento.as_view(), name="doc_eliminar"),

    url(r'^bajas_profesionales/(?P<pk>[0-9-]+)/$', views.bajas_profesionales, name="bajas_profesionales"),
    url(r'^bajas_nuevo/(?P<prof>[0-9]+)/$', BajasNuevo.as_view(), name="bajas_nuevo"),
    url(r'^bajas_modificar/(?P<pk>[0-9]+)/$', ModificarBaja.as_view(), name="bajas_modificar"),
    url(r'^bajas/(?P<pk>[0-9]+)/delete/$', EliminarBaja.as_view(), name="baja_eliminar"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

