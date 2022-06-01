from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ProfesionalForm, DocuForm, BajaForm
from .models import Profesional, Documentos, Bajas
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render
import os
from django.conf import settings



class ListadoProfesionales(ListView):
    model = Profesional
    template_name = 'listado_profesionales.html'
    context_object_name ='profesionales'

class DetalleProfesional(DetailView):
    model = Profesional
    template_name = 'detalle_profesional.html'

class ModificarProfesional(UpdateView):
    model = Profesional
    template_name = 'modificar_profesional.html'
    form_class = ProfesionalForm
    success_url = reverse_lazy('profesionales:listado_profesionales')

class NuevoProfesional(CreateView):
    model = Profesional
    template_name = 'nuevo_profesional.html'
    form_class = ProfesionalForm
    success_url = reverse_lazy('profesionales:listado_profesionales')

class EliminarProfesional(DeleteView):
    model = Profesional
    template_name = 'profesional_eliminar.html'
    success_url = reverse_lazy('profesionales:listado_profesionales')





def documentos_profesionales(request,pk):
    ext =[".jpg", ".png", "gif", ",jpeg"]
    file_path= os.path.join(settings.DJANGO_ROOT)
    print (file_path)
    print("_"*50)
    docus = Documentos.objects.filter(profesional_id=pk)
    return render(request , 'documentos_profesionales.html', context={'docs': docus, 'img_extension': ext, 'path':file_path, 'pk': pk})

class DocumentosNuevo(CreateView):
        model = Documentos
        template_name = 'formulario_docu_profesionales.html'
        form_class = DocuForm
        prof = None
        success_url = None

        def get_object(self, queryset=None):
            return queryset.get(int(prof=self.prof))

        def form_valid(self, form):
            qsProf = Profesional.objects.get(id=self.kwargs['prof'])
            form.instance.profesional = qsProf
            DocumentosNuevo.success_url = reverse('profesionales:documentos_profesionales', kwargs={'pk': self.kwargs['prof']})

            return super(DocumentosNuevo, self).form_valid(form)

        def get(self, request, *args, **kwargs):
            context = locals()
            context['prof'] = self.kwargs['prof']
            context['form'] = self.form_class

            return render(request, 'formulario_docu_profesionales.html', context)


class EliminarDocumento(DeleteView):
    model = Documentos
    template_name = 'confirm_delete_profesionales.html'
    prof = None
    success_url = None

    def delete(self, request, *args, **kwargs):
        print("."*50)
        print (self.kwargs['pk'])
        qsDocumentos = Documentos.objects.get(id=self.kwargs['pk'])
        EliminarDocumento.success_url = reverse_lazy('profesionales:documentos_profesionales', kwargs={'pk': qsDocumentos.profesional_id})
        return super(EliminarDocumento, self).delete(request, *args, **kwargs)



class ModificarDocumento(UpdateView):
    model = Documentos
    template_name = 'formulario_editar_profesionales.html'
    form_class = DocuForm
    prof = None
    success_url= None

    def form_valid(self, form):
        qsDocumentos = Documentos.objects.get(id=self.kwargs['pk'])
        qsProf = Profesional.objects.get(id = qsDocumentos.profesional_id)
        form.instance.profesional = qsProf
        ModificarDocumento.success_url = reverse('profesionales:documentos_profesionales', kwargs={'pk': qsDocumentos.profesional_id})
        return super(ModificarDocumento, self).form_valid(form)


def bajas_profesionales(request,pk):
    ext =[".jpg", ".png", "gif", ",jpeg"]
    file_path= os.path.join(settings.DJANGO_ROOT)
    print (file_path)
    print("_"*50)
    bajas = Bajas.objects.filter(profesional_id=pk)
    return render(request , 'bajas_profesionales.html', context={'bajas': bajas, 'img_extension': ext, 'path':file_path, 'pk': pk})

class BajasNuevo(CreateView):
        model = Bajas
        template_name = 'formulario_bajas_profesionales.html'
        form_class = BajaForm
        prof = None
        success_url = None

        def get_object(self, queryset=None):
            return queryset.get(int(prof=self.prof))

        def form_valid(self, form):
            qsProf = Profesional.objects.get(id=self.kwargs['prof'])
            form.instance.profesional = qsProf
            BajasNuevo.success_url = reverse('profesionales:bajas_profesionales', kwargs={'pk': self.kwargs['prof']})

            return super(BajasNuevo, self).form_valid(form)

        def get(self, request, *args, **kwargs):
            context = locals()
            context['prof'] = self.kwargs['prof']
            context['form'] = self.form_class

            return render(request, 'formulario_bajas_profesionales.html', context)


class EliminarBaja(DeleteView):
    model = Bajas
    template_name = 'confirm_delete_bajas.html'
    prof = None
    success_url = None

    def delete(self, request, *args, **kwargs):
        print("."*50)
        print (self.kwargs['pk'])
        qsBajas = Bajas.objects.get(id=self.kwargs['pk'])
        EliminarBaja.success_url = reverse_lazy('profesionales:bajas_profesionales', kwargs={'pk': qsBajas.profesional_id})
        return super(EliminarBaja, self).delete(request, *args, **kwargs)



class ModificarBaja(UpdateView):
    model = Bajas
    template_name = 'formulario_editar_bajas.html'
    form_class = BajaForm
    prof = None
    success_url= None

    def form_valid(self, form):
        qsBajas = Bajas.objects.get(id=self.kwargs['pk'])
        qsProf = Profesional.objects.get(id = qsBajas.profesional_id)
        form.instance.profesional = qsProf
        ModificarBaja.success_url = reverse('profesionales:bajas_profesionales', kwargs={'pk': qsBajas.profesional_id})
        return super(ModificarBaja, self).form_valid(form)

