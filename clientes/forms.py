from django import forms
from .models import Cliente, Documentos, Fotos


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })






class DocuForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ('cliente', 'tipodocumento', 'etiqueta', 'fecha_documento', 'documento')

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

            if field == 'cliente':
                self.fields['cliente'].widget.attrs['readonly']=True


class FotoForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ('cliente', 'etiqueta', 'fecha_foto', 'foto')

        fecha_foto = forms.DateField(
            widget = forms.DateInput(format='%m/%d/%Y'),
            input_formats=('%m/%d/%Y',)
        )


    def __init__(self, *args, **kwargs):
        super(FotoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            #if field == 'fecha':
                #self.fields['fecha'].widget.attrs[format]=('%m/%d/%Y')

            if field == 'cliente':
                self.fields['cliente'].widget.attrs['readonly']=True