from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import AlmacenForm
from .models import Almacen


class ListadoAlmacen(ListView):
    model = Almacen
    template_name = 'listado_almacen.html'
    context_object_name ='almacen'

class DetalleAlmacen(DetailView):
    model = Almacen
    template_name = 'detalle_almacen.html'

class ModificarAlmacen(UpdateView):
    model = Almacen
    template_name = 'modificar_almacen.html'
    form_class = AlmacenForm
    success_url = reverse_lazy('almacen:listado_almacen')

class NuevoAlmacen(CreateView):
    model = Almacen
    template_name = 'nuevo_almacen.html'
    form_class = AlmacenForm
    success_url = reverse_lazy('almacen:listado_almacen')

class EliminarAlmacen(DeleteView):
    model = Almacen
    template_name = 'almacen_eliminar.html'
    success_url = reverse_lazy('almacen:listado_almacen')

