from django.forms import ModelForm
from .models import Reservacion

class ReservacionForm(ModelForm):
    class Meta:
        model=Reservacion
        fields=[
            'id_reservacion',
            'nombre_titular',
            'edad',
            'pais_origen',
            'idioma',
            'check_in',
            'check_out',
            'no_adultos',
            'no_menores'
        ]
