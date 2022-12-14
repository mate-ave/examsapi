# Generated by Django 4.1.3 on 2022-11-19 02:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parcial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(choices=[('66', 'Análisis Matemático A (66)'), ('72', 'Análisis Matemático (72)'), ('51', 'Matemática (51)'), ('61', 'Matemática (61)'), ('27', 'Álgebra (27)'), ('62', 'Álgebra A (62)'), ('71', 'Álgebra (71)')], max_length=2)),
                ('anio', models.IntegerField()),
                ('cuatrimestre', models.CharField(choices=[('1', 'Primer cuatrimestre'), ('2', 'Segundo cuatrimestre')], max_length=1)),
                ('tipo_parcial', models.CharField(choices=[('1', 'Primer parcial'), ('2', 'Segundo parcial')], max_length=1)),
                ('letra', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('[A-Z]', 'La letra debe ir en mayúscula.')])),
                ('key', models.CharField(editable=False, max_length=13, unique=True)),
                ('ej_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ej1', to='parciales.ejercicio')),
                ('ej_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ej2', to='parciales.ejercicio')),
                ('ej_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ej3', to='parciales.ejercicio')),
                ('ej_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ej4', to='parciales.ejercicio')),
            ],
        ),
    ]
