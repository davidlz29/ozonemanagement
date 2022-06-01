from django import forms
from .models import Proveedor, Gasto


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })


class GastoForm(forms.ModelForm):

    class Meta:
        model = Gasto
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })
