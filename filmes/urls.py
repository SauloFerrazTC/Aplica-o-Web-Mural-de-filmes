
from django.urls import path, include
from filmes.views import ListarFilmes, FotoFilmes, CriarFilme, DeletarFilme, EditarDescricaoFilme, ListarFilmesAPI, APIDeletarFilmes, EditarAPIDescricaoFilme, CriarFilmeAPI

urlpatterns = [
path('', ListarFilmes.as_view(), name='listar-filmes'),
path('fotos/<str:arquivo>/', FotoFilmes.as_view(), name='foto-filmes'),
path('cadastroFilme/', CriarFilme.as_view(), name='criar-filmes'),
path('deletarfilme/<pk>/', DeletarFilme.as_view(), name='deletar-filmes'),
path('editar/<int:pk>/', EditarDescricaoFilme.as_view(), name='editar-filmes'),
path('comentarios/', include('comentarios.urls'), name='comentarios'),
path('api/', ListarFilmesAPI.as_view()),
path('api/<int:pk>/', APIDeletarFilmes.as_view(), name='api-deletar-filmes'),
path('api/edit/<int:pk>/', EditarAPIDescricaoFilme.as_view(), name='api-editar-filmes'),
path('api/novofilme/', CriarFilmeAPI.as_view(), name='api-criar-filmes'),
]