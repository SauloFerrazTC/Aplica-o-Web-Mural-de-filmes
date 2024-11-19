from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    CATEGORIAS = [
        ('acao', 'Ação'),
        ('comedia', 'Comédia'),
        ('drama', 'Drama'),
        ('suspense', 'Suspense'),
        ('terror', 'Terror'),
        ('ficcao', 'Ficção Científica'),
        ('romance', 'Romance'),
    ]

    titulo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    descricao = models.TextField()
    capa = models.ImageField(blank=True, null=True, upload_to='filmes/fotos')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filmes_cadastrados')

    def __str__(self):
        return self.titulo

