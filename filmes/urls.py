
from django.urls import path
from filmes.views import ListarFilmes, FotoFilmes, CriarFilme

urlpatterns = [
path('', ListarFilmes.as_view(), name='listar-filmes'),
path('fotos/<str:arquivo>/', FotoFilmes.as_view(), name='foto-filmes'),
path('cadastroFilme/', CriarFilme.as_view(), name='criar-filmes'),
]