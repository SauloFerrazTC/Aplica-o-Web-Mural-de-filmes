from django.db import models
from django.contrib.auth.models import User
from filmes.models import Filme

class Comentario(models.Model):
    coment = models.TextField(verbose_name="Comentário")
    iduser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    idfilme = models.ForeignKey(Filme, on_delete=models.CASCADE, verbose_name="Filme")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"Comentário de {self.iduser.username} no filme {self.idfilme.titulo}"

