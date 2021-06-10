from django.db import models

# Create your models here.

class Unidade(models.Model):

  nome_unidade = models.CharField(max_length=255)
  cidade = models.CharField(max_length=255)
  campus = models.CharField(max_length=255)
  endereco = models.CharField(max_length=255)

  def __str__(self):
    return str(self.nome_unidade)