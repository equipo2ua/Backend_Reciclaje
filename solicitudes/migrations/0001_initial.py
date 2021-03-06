# Generated by Django 2.0.2 on 2020-06-23 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recolector', '0001_initial'),
        ('reciclador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_material', models.CharField(max_length=50)),
                ('cantidad_material', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_reciclaje', models.TimeField()),
                ('fecha_reciclaje', models.DateField()),
                ('peso_total_materiales', models.IntegerField(blank=True, null=True)),
                ('volumen_total_materiales', models.IntegerField(blank=True, null=True)),
                ('notificaciones_rechazadas', models.CharField(max_length=12)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('id_reciclador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reciclador.Reciclador')),
                ('id_recolector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recolector.Recolector')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solitudes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=12)),
                ('id_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.Material')),
                ('id_solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.Solicitud')),
            ],
            options={
                'verbose_name': 'Tipo_material',
                'verbose_name_plural': 'Tipo_materiales',
            },
        ),
    ]
