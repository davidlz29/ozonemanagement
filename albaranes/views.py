from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import AlbaranForm
from pedidos.models import Pedido
from .models import Albaran
from articulos .models import ArticuloPedido
from clientes.models import Cliente
from django.shortcuts import render



class ListadoAlbaranes(ListView):
    model = Albaran
    template_name = 'listado_albaranes.html'
    context_object_name ='albaranes'


class ModificarAlbaran(UpdateView):
    model = Albaran
    template_name = 'modificar_albaran.html'
    form_class = AlbaranForm
    success_url = reverse_lazy('albaranes:listado_albaranes')

class NuevoAlbaran(CreateView):
    model = Albaran
    template_name = 'nuevo_albaran.html'
    form_class = AlbaranForm
    success_url = reverse_lazy('albaranes:listado_albaranes')


class EliminarAlbaran(DeleteView):
    model=Albaran
    template_name = 'albaran_eliminar.html'
    success_url = reverse_lazy('albaranes:listado_albaranes')



def DetalleAlbaran(request, pk):

    albaran = Albaran.objects.get(pk=pk)

    articulo = ArticuloPedido.objects.filter(cod_pedido=albaran.pedido)

    return render(request, 'detalle_albaran.html', context={'albaran': albaran,'articulo': articulo, 'pk':pk})
