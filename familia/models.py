from django.db import models

# Create your models here.


class FamiliaMiembro(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()


class Propiedad(models.Model):
    nombre = models.CharField(max_length=128)
    familia_miembro = models.ForeignKey('FamiliaMiembro', on_delete=models.CASCADE, null=True )

    