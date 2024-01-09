# Generated by Django 5.0.1 on 2024-01-09 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255)),
                ('tamano', models.IntegerField(blank=True, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('aforo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('identificador', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('personas', models.IntegerField(blank=True, null=True)),
                ('sala', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_backend.sala')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_backend.usuario')),
            ],
        ),
    ]