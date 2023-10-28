from rest_framework import generics
from .models import PessoaProfissional, Consulta
from .serializers import PessoaProfissionalSerializer, ConsultaSerializer

class PessoaProfissionalListCreateView(generics.ListCreateAPIView):
    queryset = PessoaProfissional.objects.all()
    serializer_class = PessoaProfissionalSerializer

class PessoaProfissionalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PessoaProfissional.objects.all()
    serializer_class = PessoaProfissionalSerializer

class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer