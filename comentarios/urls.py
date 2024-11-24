
from django.urls import path
from comentarios.views import ListarComentarios, CriarComentario, DeletarComentarios, EditarComentario

urlpatterns = [
path('<int:filme_id>/', ListarComentarios.as_view(), name='listar-comentarios'),
path('<int:filme_id>/addcoment/', CriarComentario.as_view(), name='criar-comentarios'),
path('deletar/<int:pk>/', DeletarComentarios.as_view(), name='deletar-comentarios'),
path('editar/<int:pk>/', EditarComentario.as_view(), name='editar-comentarios'),
]