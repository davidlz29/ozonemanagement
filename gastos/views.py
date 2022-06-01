from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import ProveedorForm , GastoForm
from .models import Proveedor, Gasto



class ListadoProveedores(ListView):
    model = Proveedor
    template_name = 'listado_proveedores.html'
    context_object_name ='proveedores'

class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = 'detalle_proveedor.html'

class ModificarProveedor(UpdateView):
    model = Proveedor
    template_name = 'modificar_proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('gastos:listado_proveedores')

class NuevoProveedor(CreateView):
    model = Proveedor
    template_name = 'nuevo_proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('gastos:listado_proveedores')

class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'proveedor_eliminar.html'
    success_url = reverse_lazy('gastos:listado_proveedores')




class ListadoGastos(ListView):
    model = Gasto
    template_name = 'listado_gastos.html'
    context_object_name ='gastos'

class DetalleGasto(DetailView):
    model = Gasto
    template_name = 'detalle_gasto.html'

class ModificarGasto(UpdateView):
    model = Gasto
    template_name = 'modificar_gasto.html'
    form_class = GastoForm
    success_url = reverse_lazy('gastos:listado_gastos')

class NuevoGasto(CreateView):
    model = Gasto
    template_name = 'nuevo_gasto.html'
    form_class = GastoForm
    success_url = reverse_lazy('gastos:listado_gastos')

class EliminarGasto(DeleteView):
    model = Gasto
    template_name = 'gasto_eliminar.html'
    success_url = reverse_lazy('gastos:listado_gastos')


