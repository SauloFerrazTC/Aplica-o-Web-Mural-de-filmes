
from django.urls import path
from comentarios.views import ListarComentarios, CriarComentario

urlpatterns = [
path('<int:filme_id>/', ListarComentarios.as_view(), name='listar-comentarios'),
path('<int:filme_id>/addcoment/', CriarComentario.as_view(), name='criar-comentarios'),
]