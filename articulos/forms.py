from django import forms
from .models import Articulo, Categoria


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })



class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })
