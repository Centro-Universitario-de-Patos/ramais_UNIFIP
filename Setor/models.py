from django.db import models
from Colaborador.models import Colaborador
from Unidade.models import Unidade
class Setor(models.Model):
    nome_setor = models.CharField(max_length=250)
    ramal = models.IntegerField()
    bloco = models.CharField(max_length=2)
    horario_funcionamento_inicio_turno1 = models.TimeField()
    horario_funcionamento_final_tuno1 = models.TimeField()
    parada = models.BooleanField()
    horario_funcionamento_inicio_turno2 = models.TimeField()
    horario_funcionamento_final_tuno2 = models.TimeField()
    unidade = models.ManyToManyField(Unidade)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.nome_setor)