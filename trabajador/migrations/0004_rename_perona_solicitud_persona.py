# Generated by Django 4.1.5 on 2023-03-07 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0003_alter_persona_apellido_alter_persona_curp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='perona',
            new_name='persona',
        ),
    ]