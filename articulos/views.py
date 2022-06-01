
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import ArticuloForm, CategoriaForm
from .models import Articulo, Categoria


class ListadoArticulos(ListView):
    model = Articulo
    template_name = 'listado_articulos.html'
    context_object_name = 'articulos'

class DetalleArticulo(DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'

class ModificarArticulo(UpdateView):
    model = Articulo
    template_name = 'modificar_articulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('articulos:listado_articulos')

class NuevoArticulo(CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('articulos:listado_articulos')

class EliminarArticulo(DeleteView):
    model = Articulo
    template_name = 'articulo_eliminar.html'
    success_url = reverse_lazy('articulos:listado_articulos')


class ListadoCategorias(ListView):
    model = Categoria
    template_name = 'listado_categorias.html'
    context_object_name = 'categorias'

class DetalleCategoria(DetailView):
    model = Categoria
    template_name = 'detalle_categoria.html'

class ModificarCategoria(UpdateView):
    model = Categoria
    template_name = 'modificar_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('articulos:listado_categorias')

class NuevaCategoria(CreateView):
    model = Categoria
    template_name = 'nueva_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('articulos:listado_categorias')

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'categoria_eliminar.html'
    success_url = reverse_lazy('articulos:listado_categorias')