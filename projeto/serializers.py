
from rest_framework import serializers
from django.contrib.auth.models import User

class CadastroUsuarioSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def validate(self, dados):
        
        if dados['password1'] != dados['password2']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return dados

    def create(self, dados_validados):
        
        dados_validados.pop('password2')
        
        usuario = User.objects.create_user(
            username=dados_validados['username'],
            password=dados_validados['password1']
        )
        return usuario