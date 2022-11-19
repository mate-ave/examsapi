from rest_framework import serializers
from parciales.models import Ejercicio, Parcial


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ['enunciado']


class ParcialSerializer(serializers.ModelSerializer):
    ej_1 = EjercicioSerializer()
    ej_2 = EjercicioSerializer()
    ej_3 = EjercicioSerializer()
    ej_4 = EjercicioSerializer()

    class Meta:
        model = Parcial
        fields = ['id', 'materia', 'anio', 'cuatrimestre',
                  'tipo_parcial', 'letra', 'ej_1', 'ej_2', 'ej_3', 'ej_4']


class ParcialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcial
        fields = ['id', 'materia', 'anio',
                  'cuatrimestre', 'tipo_parcial', 'letra']
