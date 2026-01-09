from django.db import models
from django.contrib.auth.models import User

class Provincia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Municipio(models.Model):
    nome = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='municipios')

    def __str__(self):
        return f"{self.nome} - {self.provincia.nome}"


class Contacto(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    observacoes = models.TextField(blank=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contactos')
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
