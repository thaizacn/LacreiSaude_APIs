from django.db import models

class PessoaProfissional(models.Model):
    #Campos da tabela do BD
    nome = models.CharField(max_length=100)
    #O cadastro aceita o campo Nome Social.
    nome_social = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    #Campos da tabela do BD
    data = models.DateField()
    profissional = models.ForeignKey(PessoaProfissional, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta em {self.data} com {self.profissional}"
