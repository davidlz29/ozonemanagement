from django import forms
from .models import Almacen


class AlmacenForm(forms.ModelForm):

    class Meta:
        model = Almacen
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(AlmacenForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })



