# Generated by Django 2.0.2 on 2020-06-23 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial_Recolector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_finalizado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historiales',
            },
        ),
        migrations.CreateModel(
            name='Recolector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_recolector', models.CharField(max_length=50)),
                ('apellido_recolector', models.CharField(max_length=50)),
                ('correo_recolector', models.EmailField(max_length=254)),
                ('telefono_recolector', models.CharField(max_length=50)),
                ('calificacion_recolector', models.FloatField()),
                ('estado', models.IntegerField()),
                ('cantidad_calificaciones', models.FloatField()),
                ('suma_calificaciones', models.FloatField()),
            ],
            options={
                'verbose_name': 'Recolector',
                'verbose_name_plural': 'Recolectores',
                'ordering': ['nombre_recolector'],
            },
        ),
        migrations.AddField(
            model_name='historial_recolector',
            name='id_recolector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recolector.Recolector'),
        ),
    ]
