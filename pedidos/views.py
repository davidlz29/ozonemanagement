from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import PedidoForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Pedido
from articulos.models import ArticuloPedido, Articulo
from django.shortcuts import render



class ListadoPedidos(ListView):
    model = Pedido
    template_name = 'listado_pedidos.html'
    context_object_name ='pedidos'


class NuevoPedido(CreateView):
    model = Pedido
    template_name = 'nuevo_pedido.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:listado_pedidos')

class ModificarPedido(UpdateView):
    model = Pedido
    template_name = 'modificar_pedido.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:listado_pedidos')

class EliminarPedido(DeleteView):
    model=Pedido
    template_name = 'pedido_eliminar.html'
    success_url = reverse_lazy('pedidos:listado_pedidos')


def AddArticuloPedido(request,pk):

    pedido = Pedido.objects.get(pk=pk)

    lstarticulos=""

    if request.POST:

        articulo=request.POST["articulos"]

        idart = Articulo.objects.get(id=articulo)

        cantidad=request.POST["cantidad"]


        u = ArticuloPedido.objects.create(cod_pedido=pedido, cod_articulo=idart, cantidad=cantidad)

        lstarticulos=ArticuloPedido.objects.filter(cod_pedido=pedido)

    return render(request, 'add_articulos.html', context={'form': PedidoForm(),'articulos': lstarticulos, 'pk':pk})




def DetalleArticuloPedido(request, pk):

    pedido = Pedido.objects.get(pk=pk)

    articulo = ArticuloPedido.objects.filter(cod_pedido=pedido)

    return render(request, 'detalle_pedido.html', context={'pedido': pedido, 'articulo': articulo, 'pk':pk})
