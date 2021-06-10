from django.contrib import admin
from .models import Colaborador


@admin.register(Colaborador)
class Admin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'instagram', 'linkedin')
