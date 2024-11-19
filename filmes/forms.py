from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano', 'descricao', 'capa', 'categoria']


class FilmeDescricaoForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['descricao']  # Apenas o campo de descrição será exibido

    def __init__(self, *args, **kwargs):
        super(FilmeDescricaoForm, self).__init__(*args, **kwargs)
        # Desabilita os outros campos (não exibimos eles)
        self.fields['descricao'].widget.attrs['placeholder'] = 'Digite a nova descrição...'