from rest_framework import serializers
from .models import Filme
from drf_extra_fields.fields import Base64ImageField

class FilmeSerializer(serializers.ModelSerializer):
    
    capa = Base64ImageField(required=False, represent_in_base64=True)  

    class Meta:
        model = Filme
        fields = '__all__'  

class FilmeDescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['descricao']


class CriarFilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano', 'descricao', 'capa', 'categoria']