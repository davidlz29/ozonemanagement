from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render
import os
from django.conf import settings
from .forms import ClienteForm, DocuForm, FotoForm
from .models import Cliente, Documentos, Fotos



class ListadoClientes(ListView):
    model = Cliente
    template_name = 'listado_clientes.html'
    context_object_name ='clientes'

class DetalleCliente(DetailView):
    model = Cliente
    template_name = 'detalle_cliente.html'

class ModificarCliente(UpdateView):
    model = Cliente
    template_name = 'modificar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:listado_clientes')

class NuevoCliente(CreateView):
    model = Cliente
    template_name = 'nuevo_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:listado_clientes')

class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'cliente_eliminar.html'
    success_url = reverse_lazy('clientes:listado_clientes')






def documentos_cliente(request,pk):
    ext = [".jpg", ".png", "gif", ",jpeg"]
    file_path = os.path.join(settings.DJANGO_ROOT)
    print(file_path)
    print("_" * 50)
    docus = Documentos.objects.filter(cliente_id=pk)
    return render(request, 'documentos.html', context={'docs': docus, 'img_extension': ext, 'path':file_path, 'pk': pk})


class DocumentosNuevo(CreateView):
    model = Documentos
    template_name = 'formulario_docu.html'
    form_class = DocuForm
    client = None
    success_url= None


    def get_object(self, queryset=None):
        return queryset.get(int(client=self.client))

    def form_valid(self, form):
        qsClient = Cliente.objects.get(id=self.kwargs['client'])
        form.instance.cliente = qsClient
        DocumentosNuevo.success_url = reverse('clientes:documentos_cliente', kwargs={'pk': self.kwargs['client']})

        return super(DocumentosNuevo, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        context=locals()
        context['client']=self.kwargs['client']
        context['form'] =self.form_class

        return render(request, 'formulario_docu.html', context)


class EliminarDocumento(DeleteView):
    model = Documentos
    template_name = 'doc_confirm_delete.html'
    client = None
    success_url = None

    def delete(self, request, *args, **kwargs):
        print("."*50)
        print (self.kwargs['pk'])
        qsDocumentos = Documentos.objects.get(id=self.kwargs['pk'])
        EliminarDocumento.success_url = reverse_lazy('clientes:documentos_cliente', kwargs={'pk': qsDocumentos.cliente_id})
        return super(EliminarDocumento, self).delete(request, *args, **kwargs)


class ModificarDocumento(UpdateView):
    model = Documentos
    template_name = 'formulario_doc_editar.html'
    form_class = DocuForm
    client = None
    success_url= None

    def form_valid(self, form):
        qsDocumentos = Documentos.objects.get(id=self.kwargs['pk'])
        qsClient = Cliente.objects.get(id = qsDocumentos.cliente_id)
        form.instance.cliente = qsClient
        ModificarDocumento.success_url = reverse('clientes:documentos_cliente', kwargs={'pk': qsDocumentos.cliente_id})
        return super(ModificarDocumento, self).form_valid(form)





def fotos_cliente(request,pk):
    ext = [".jpg", ".png", "gif", ",jpeg"]
    file_path = os.path.join(settings.DJANGO_ROOT)
    print(file_path)
    print("_" * 50)
    fotos = Fotos.objects.filter(cliente_id=pk)
    return render(request, 'fotos.html', context={'fotos': fotos, 'img_extension': ext, 'path':file_path, 'pk': pk})


class FotoNueva(CreateView):
    model = Fotos
    template_name = 'formulario_foto.html'
    form_class = FotoForm
    client = None
    success_url= None


    def get_object(self, queryset=None):
        return queryset.get(int(client=self.client))

    def form_valid(self, form):
        qsClient = Cliente.objects.get(id=self.kwargs['client'])
        form.instance.cliente = qsClient
        FotoNueva.success_url = reverse('clientes:fotos_cliente', kwargs={'pk': self.kwargs['client']})

        return super(FotoNueva, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        context=locals()
        context['client']=self.kwargs['client']
        context['form'] =self.form_class

        return render(request, 'formulario_foto.html', context)


class EliminarFoto(DeleteView):
    model = Fotos
    template_name = 'foto_confirm_delete.html'
    client = None
    success_url = None

    def delete(self, request, *args, **kwargs):
        print("."*50)
        print (self.kwargs['pk'])
        qsFotos = Fotos.objects.get(id=self.kwargs['pk'])
        EliminarFoto.success_url = reverse_lazy('clientes:fotos_cliente', kwargs={'pk': qsFotos.cliente_id})
        return super(EliminarFoto, self).delete(request, *args, **kwargs)


class ModificarFoto(UpdateView):
    model = Fotos
    template_name = 'formulario_foto_editar.html'
    form_class = FotoForm
    client = None

    def form_valid(self, form):
        qsFotos = Fotos.objects.get(id=self.kwargs['pk'])
        qsClient = Cliente.objects.get(id = qsFotos.cliente_id)
        form.instance.cliente = qsClient
        ModificarFoto.success_url = reverse_lazy('clientes:fotos_cliente', kwargs={'pk': qsFotos.cliente_id})
        return super(ModificarFoto, self).form_valid(form)


