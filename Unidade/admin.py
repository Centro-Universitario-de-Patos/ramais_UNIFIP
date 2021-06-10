from django.contrib import admin
from .models import Unidade
# Register your models here.

@admin.register (Unidade)

class NameAdmin(admin.ModelAdmin):
    list_display = ('nome_unidade','cidade', 'campus', 'endereco')


