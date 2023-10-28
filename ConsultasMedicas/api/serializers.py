from rest_framework import serializers
from .models import PessoaProfissional, Consulta

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    #Definindo metadados para o serializador
    class Meta:
        model = PessoaProfissional
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        #Definindo metadados para o serializador
        model = Consulta
        fields = '__all__'