from django.conf import settings
from django.views.generic import View 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .forms import CustomUserCreationForm

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
            return redirect('index')  # Redireciona para a página inicial após o cadastro
        else:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")

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
