from django import forms
from .models import Vuelo

class FormsVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['id','nombre', 'tipo_vuelo', 'precio']
        widgets = {
            'tipo_vuelo': forms.Select(choices=Vuelo.tipo_vuelo),
        }