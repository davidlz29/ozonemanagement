from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.static import serve
from . import views

urlpatterns = [


url('albaranes/', include('albaranes.urls', namespace='albaranes')),
    url('articulos/', include('articulos.urls', namespace='articulos')),
    url('clientes/', include('clientes.urls', namespace='clientes')),
    url('pedidos/', include('pedidos.urls', namespace='pedidos')),
    url('almacen/', include('almacen.urls', namespace='almacen')),
    url('gastos/', include('gastos.urls', namespace='gastos')),
    url('profesionales/', include('profesionales.urls', namespace='profesionales')),


    path('admin/', admin.site.urls),
    url(r'^login/', auth_views.LoginView.as_view(), {'template_name': 'templates/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'template_name': 'templates/logged_out.html'}, name='logout'),
    url(r'^', views.index),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)