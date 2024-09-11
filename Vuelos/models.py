from django.db import models

# Create your models here.
class Vuelo(models.Model):
    nacional = 'Nacional'
    internacional = 'Internacional'
    tipo_vuelo2= [
        (nacional, 'Nacional'),
        (internacional, 'Internacional'),
    ]
    id = models.IntegerField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_vuelo = models.CharField(max_length=15, choices=tipo_vuelo2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name