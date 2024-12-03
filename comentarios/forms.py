from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['coment']  

    def save(self, user, filme, commit=True):
        comentario = super().save(commit=False)
        comentario.iduser = user  # Define o usuário logado
        comentario.idfilme = filme  # Define o filme relacionado
        if commit:
            comentario.save()
        return comentario
        
class EditarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['coment']
        widgets = {
            'coment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Edite seu comentário...',
                'rows': 4,
            }),
        }
