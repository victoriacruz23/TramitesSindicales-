from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Rol(models.Model):
    nombre = models.CharField(max_length=20)


class Empresa(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la Empresa')
    razon_social = models.CharField(max_length=40, verbose_name='Razon Social')
    direccion = models.CharField(max_length=200, verbose_name='Direccion')
    correro_electonico = models.CharField(max_length=200, verbose_name='Correo Electronico')
    telefono = models.CharField(max_length=20, verbose_name='Numero de telefono')

    def __str__(self):
        return f'{self.nombre}'

class Persona(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    nombre = models.CharField(max_length=50,null=True,blank=True)
    apellido = models.CharField(max_length=50,null=True,blank=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    numero_telefono = models.CharField(max_length=10,null=True,blank=True)
    numero_colaborador = models.CharField(max_length=10,null=True,blank=True)
    profecion = models.CharField(max_length=50,null=True,blank=True)
    curp = models.CharField(max_length=50,null=True,blank=True)
    rfc = models.CharField(max_length=15,null=True,blank=True)
    fecha_validacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.nombre}'


class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50,null=True,blank=True)
    numero_contrato = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    fecha_expiracion = models.DateField()


class Credencial(models.Model):
    solicitud = models.OneToOneField(Solicitud,on_delete=models.CASCADE)
    actanacimiento = models.FileField(upload_to='actanacimiento/%Y/%m/%d',null=True,blank=True, verbose_name='Acta de Nacimineto')
    fotopersona = models.ImageField(upload_to='fotopersona/%Y/%m/%d',null=True,blank=True, verbose_name='Foto Personal')
    firma = models.FileField(upload_to='firma/%Y/%m/%d',null=True,blank=True, verbose_name='Foto firma')

class Tramite(models.Model):
    nombre = models.CharField(max_length=50)


class Seguimiento(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    tipo_tramite = models.ForeignKey(Tramite, on_delete=models.PROTECT)
    observacion = models.CharField(max_length=200)
    fecha_resolucion = models.DateField()


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
    fecha_contrato = models.DateField()
    fecha_finalizacion = models.DateField()
