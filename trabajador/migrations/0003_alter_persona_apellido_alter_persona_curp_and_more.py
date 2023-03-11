# Generated by Django 4.1.5 on 2023-03-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0002_empresa_persona_rol_tramite_solicitud_seguimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='curp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_validacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero_colaborador',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero_telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='profecion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rfc',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]