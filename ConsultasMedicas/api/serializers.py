from rest_framework import serializers
from .models import PessoaProfissional, Consulta

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    #Definindo metadados para o serializador
    class Meta:
        model = PessoaProfissional
        fields = ('id', 'nome', 'nome_social')
        extra_kwargs = {
            'nome': {'max_length': 100},
            'nome_social': {'max_length': 100, 'required': False}
        }

    def validate_nome(self, value):
        # Verifica se o nome contém apenas letras e espaços
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Nome deve conter apenas letras e espaços.")
        return value

    def validate_nome_social(self, value):
        # Verifica se o nome social contém apenas letras e espaços
        if value and not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Nome social deve conter apenas letras e espaços.")
        return value

class ConsultaSerializer(serializers.ModelSerializer):
        #Definindo metadados para o serializador
    class Meta:
        model = Consulta
        fields = ('id', 'data', 'profissional')
        extra_kwargs = {
            'data': {'required': True},
            'profissional': {'required': True}
        }

    def validate_data(self, value):
        # Verifica se a data está no futuro (não permite agendamentos no passado)
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("A data da consulta deve ser no futuro.")
        return value