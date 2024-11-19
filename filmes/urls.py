
from django.urls import path
from filmes.views import ListarFilmes, FotoFilmes, CriarFilme, DeletarFilme, EditarDescricaoFilme

urlpatterns = [
path('', ListarFilmes.as_view(), name='listar-filmes'),
path('fotos/<str:arquivo>/', FotoFilmes.as_view(), name='foto-filmes'),
path('cadastroFilme/', CriarFilme.as_view(), name='criar-filmes'),
path('deletarfilme/<pk>/', DeletarFilme.as_view(), name='deletar-filmes'),
path('editar/<int:pk>/', EditarDescricaoFilme.as_view(), name='editar-filmes'),
]