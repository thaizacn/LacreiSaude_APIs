from rest_framework.test import APITestCase
from rest_framework import status
from .models import PessoaProfissional, Consulta
from .serializers import PessoaProfissionalSerializer, ConsultaSerializer
from datetime import date, timedelta

class PessoaProfissionalTests(APITestCase):
    def test_criar_pessoa_profissional(self):
        data = {'nome': 'Thaiza', 'nome_social': 'Thaiza Social'}
        response = self.client.post('/api/profissionais/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_pessoa_profissional(self):
        PessoaProfissional.objects.create(nome='Thaiza', nome_social='Thaiza Social')
        response = self.client.get('/api/profissionais/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_nome_contem_apenas_letras_e_espacos(self):
        serializer = PessoaProfissionalSerializer(data={'nome': 'Alice123', 'nome_social': 'Alice Social'})
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome', serializer.errors)

    def test_nome_social_contem_apenas_letras_e_espacos(self):
        serializer = PessoaProfissionalSerializer(data={'nome': 'Alice', 'nome_social': 'Alice123'})
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome_social', serializer.errors)

class ConsultaTests(APITestCase):
    def test_criar_consulta(self):
        profissional = PessoaProfissional.objects.create(nome='Thaiza', nome_social='Thaiza Social')
        data = {'data': '2023-11-01', 'profissional': profissional.id}
        response = self.client.post('/api/consultas/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_consulta(self):
        profissional = PessoaProfissional.objects.create(nome='Thaiza', nome_social='Thaiza Social')
        Consulta.objects.create(data='2023-11-01', profissional=profissional)
        response = self.client.get('/api/consultas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

#    def test_data_no_futuro(self):
#        data_passada = date.today() - timedelta(days=1)  # Data passada
#        serializer = ConsultaSerializer(data={'data': data_passada, 'profissional': self.profissional.id})
#        self.assertFalse(serializer.is_valid())
#        self.assertIn('data', serializer.errors)