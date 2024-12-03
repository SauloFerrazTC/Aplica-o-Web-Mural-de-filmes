from rest_framework import serializers
from .models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='iduser.username', read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'coment', 'username', 'idfilme', 'iduser']


class ComentarioEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['coment']        