from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Trabajador(models.Model):
    # `user = models.ForeignKey(
    #     User, verbose_name='Usuario', on_delete=models.CASCADE)`
    nombre = models.CharField(
        verbose_name='Nombre del Trabajador', max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=250)
    edad = models.PositiveIntegerField(default=0)
    estado_civil = models.BooleanField(
        default=True, verbose_name='Estado Civil')
    fecha_de_nacimiento = models.DateField(
        default=datetime.now, verbose_name='Fecha de nacimiento')
    fecha_contrato=models.DateField()
    fecha_finalizacion=models.DateField()

    
