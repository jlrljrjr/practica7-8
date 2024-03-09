from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Opciones_idioma = [
    ('es', 'Español'),
    ('en', 'Ingles'),
    ('fr', 'Frances'),
    ('de', 'Aleman'),
    ('cn', 'Mandarin'),
    ('ot', 'Otro'),
]

class Reservacion(models.Model):
    id_reservacion= models.IntegerField()
    nombre_titular = models.CharField(max_length=512)
    edad = models.IntegerField()
    pais_origen = models.CharField(max_length=512)
    idioma = models.CharField(max_length=2, choices=Opciones_idioma)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    no_adultos = models.IntegerField()
    no_menores = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre_titular} - {self.no_adultos} adultos, {self.no_menores} menores'
    