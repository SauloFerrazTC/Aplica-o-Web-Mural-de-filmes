
from django.urls import path
from comentarios.views import ListarComentarios, CriarComentario, DeletarComentarios, EditarComentario, ListarComentariosAPI, APIDeletarComentario, EditarAPIComentario, CriarComentarioAPI

urlpatterns = [
path('<int:filme_id>/', ListarComentarios.as_view(), name='listar-comentarios'),
path('<int:filme_id>/addcoment/', CriarComentario.as_view(), name='criar-comentarios'),
path('deletar/<int:pk>/', DeletarComentarios.as_view(), name='deletar-comentarios'),
path('editar/<int:pk>/', EditarComentario.as_view(), name='editar-comentarios'),
path('api/<int:filme_id>/', ListarComentariosAPI.as_view()),
path('api/deletar/<int:pk>/', APIDeletarComentario.as_view(), name='api-deletar-comentario'),
path('api/edit/<int:pk>/', EditarAPIComentario.as_view(), name='api-editar-comentario'),
path('api/addcoment/', CriarComentarioAPI.as_view(), name='api-criar-comentario'),
]