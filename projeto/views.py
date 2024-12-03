from django.conf import settings
from django.views.generic import View 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .forms import CustomUserCreationForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from .serializers import CadastroUsuarioSerializer
from rest_framework.views import APIView
from rest_framework import status


class Login(View):

    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/filmes")
        return render(request, 'login.html', contexto)

    def post(self, request):

        nome = request.POST.get('nome', None)
        senha = request.POST.get('senha', None)

        user = authenticate(request, username=nome, password=senha)
        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect("/filmes")

            return render(request, 'login.html', {'mensagem': 'Usuário inativo'})

        return render(request, 'login.html', {'mensagem': 'Usuário ou senha errados'})     


class Cadastro(View):

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('index')  
        else:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            
            return render(request, 'cadastro.html', {'form': form})

    def get(self, request):
        
        form = CustomUserCreationForm()
        return render(request, 'cadastro.html', {'form': form})

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)    

class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name or user.username,  
            'email': user.email,
            'token': token.key
        })    


class CadastroUsuarioAPI(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        serializer = CadastroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(
                {"mensagem": "Usuário cadastrado com sucesso!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)