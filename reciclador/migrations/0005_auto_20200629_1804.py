# Generated by Django 2.2 on 2020-06-29 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reciclador', '0004_auto_20200627_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reciclador',
            old_name='calificacion_recolector',
            new_name='calificacion_reciclador',
        ),
    ]