from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Ejercicio(models.Model):
    enunciado = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.enunciado


class Parcial(models.Model):
    MATERIAS = (
        ('66', 'Análisis Matemático A (66)'),
        ('72', 'Análisis Matemático (72)'),
        ('51', 'Matemática (51)'),
        ('61', 'Matemática (61)'),
        ('27', 'Álgebra (27)'),
        ('62', 'Álgebra A (62)'),
        ('71', 'Álgebra (71)'),
    )
    materia = models.CharField(max_length=2, choices=MATERIAS, null=False, blank= False)
    anio = models.IntegerField(null=False, blank= False)
    CUATRIMESTRES = (
        ('1', 'Primer cuatrimestre'),
        ('2', 'Segundo cuatrimestre'),
    )
    cuatrimestre = models.CharField(max_length=1, choices=CUATRIMESTRES, null=False, blank= False)
    TIPO_PARCIAL = (
        ('1', 'Primer parcial'),
        ('2', 'Segundo parcial'),
    )
    tipo_parcial = models.CharField(max_length=1, choices=TIPO_PARCIAL, null=False, blank= False)
    letra = models.CharField(max_length=1, blank=False, null=False,
     validators=[RegexValidator('[A-Z]',
                               'La letra debe ir en mayúscula.')])
    key = models.CharField(max_length=13, unique=True, editable=False)
    ej_1 = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='ej1', null=False, blank= False)
    ej_2 = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='ej2', null=False, blank= False)
    ej_3 = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='ej3', null=False, blank= False)
    ej_4 = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='ej4', null=False, blank= False)

    def __str__(self):
        return self.materia + " - " + str(self.anio) + " - " + self.cuatrimestre + " - " + self.tipo_parcial + " - " + self.letra

    def save(self, *args, **kwargs):
        self.key = self.materia + "-" + str(self.anio) + "-" + self.cuatrimestre + "-" + self.tipo_parcial + "-" + self.letra
        super(Parcial, self).save(*args, **kwargs)