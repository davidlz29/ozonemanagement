from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })
