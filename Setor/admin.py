from django.contrib import admin
from .models import Setor
@admin.register(Setor)
class Admin(admin.ModelAdmin):
   list_display = ('nome_setor', 'ramal', 'bloco', 'horario_funcionamento_inicio_turno1', 'horario_funcionamento_final_tuno1', 'parada', 'horario_funcionamento_inicio_turno2', 'horario_funcionamento_final_tuno2')
