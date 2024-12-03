from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano', 'descricao', 'capa', 'categoria']


class FilmeDescricaoForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['descricao']  

    def __init__(self, *args, **kwargs):
        super(FilmeDescricaoForm, self).__init__(*args, **kwargs)
        
        self.fields['descricao'].widget.attrs['placeholder'] = 'Digite a nova descrição...'