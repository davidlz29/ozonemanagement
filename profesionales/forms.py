from django import forms
from .models import Profesional, Documentos, Bajas


class ProfesionalForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(ProfesionalForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })



class DocuForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ('profesional', 'tipodocumento', 'etiqueta', 'fecha_documento', 'documento')

        fecha_documento = forms.DateField(
            widget = forms.DateInput(format='%m/%d/%Y'),
            input_formats=('%m/%d/%Y',)
        )


    def _init_(self, *args, **kwargs):
        super(DocuForm, self)._init_(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            if field == 'profesional':
                self.fields['profesional'].widget.attrs['readonly']=True


class BajaForm(forms.ModelForm):
    class Meta:
        model = Bajas
        fields = ('profesional', 'etiqueta', 'fecha_documento', 'bajas')

        fecha_documento = forms.DateField(
            widget = forms.DateInput(format='%m/%d/%Y'),
            input_formats=('%m/%d/%Y',)
        )


    def _init_(self, *args, **kwargs):
        super(BajaForm, self)._init_(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            if field == 'profesional':
                self.fields['profesional'].widget.attrs['readonly']=True

