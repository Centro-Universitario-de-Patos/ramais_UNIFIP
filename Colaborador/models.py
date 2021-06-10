from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    celular = models.CharField(max_length=20)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nome)

