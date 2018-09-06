from django.db import models
from registrees.apps.relationtp.mixins import TimeStampedModel


# Modelo parques
class Park(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()


# Modelo arboles
class Tree(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    edad_aproximada = models.IntegerField()
    parque = models.ForeignKey(Park, null=True)
