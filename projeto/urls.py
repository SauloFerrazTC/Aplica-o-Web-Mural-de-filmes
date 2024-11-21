"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from projeto.views import Login, Logout, Cadastro, Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', Cadastro.as_view(), name='cadastrar_usuario'),
    path('login/', Login.as_view(), name='login_usuario'),
    path('logout/', Logout.as_view(), name='logout_usuario'),
    path('filmes/', include('filmes.urls'), name='filmes'),
    path('comentarios/', include('comentarios.urls'), name='comentarios'),
    path('', Index.as_view(), name='index'),  # URL para a página inicial
]
