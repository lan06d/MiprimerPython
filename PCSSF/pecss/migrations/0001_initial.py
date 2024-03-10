# Generated by Django 5.0.2 on 2024-03-05 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(max_length=50)),
                ('numeroIdentificacion', models.IntegerField()),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('direecion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(max_length=50)),
                ('valor_servicio', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipoDocumento', models.CharField(max_length=50)),
                ('numDocumento', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMascota', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('observacion', models.TextField()),
                ('fk_ID_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecss.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('observacion', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('fk_id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecss.mascota')),
                ('fk_id_tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecss.tiposervicio')),
                ('fk_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecss.usuario')),
            ],
        ),
    ]