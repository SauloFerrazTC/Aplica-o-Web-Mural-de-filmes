from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['coment']  # Só o comentário será preenchido pelo usuário

    def save(self, user, filme, commit=True):
        comentario = super().save(commit=False)
        comentario.iduser = user  # Define o usuário logado
        comentario.idfilme = filme  # Define o filme relacionado
        if commit:
            comentario.save()
        return comentario
