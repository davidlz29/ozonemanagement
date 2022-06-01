from django import forms
from .models import Albaran

class AlbaranForm(forms.ModelForm):

    class Meta:
        model = Albaran
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(AlbaranForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control border-primary'
            })


