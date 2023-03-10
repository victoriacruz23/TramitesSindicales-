# Generated by Django 4.1.5 on 2023-02-16 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Trabajador')),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=250)),
                ('edad', models.PositiveIntegerField(default=0)),
                ('estado_civil', models.BooleanField(default=True, verbose_name='Estado Civil')),
                ('fecha_de_nacimiento', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('fecha_contrato', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
            ],
        ),
    ]
