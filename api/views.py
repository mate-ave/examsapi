from rest_framework import generics
from .serializers import ParcialSerializer, ParcialInfoSerializer
from parciales.models import Parcial

class ParcialesList(generics.ListAPIView):
    serializer_class = ParcialSerializer
    def get_queryset(self):
        return Parcial.objects.all()

class ParcialesMateriaList(generics.ListAPIView):
    serializer_class = ParcialInfoSerializer
    def get_queryset(self):
        materia = self.kwargs["materia"]
        return Parcial.objects.filter(materia=materia)

class ParcialDetailView(generics.RetrieveAPIView):
    serializer_class = ParcialSerializer
    def get_queryset(self):
        return Parcial.objects.all()