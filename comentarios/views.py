# Create your views here.
from django.views.generic import View, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from comentarios.models import Comentario
from .forms import ComentarioForm
from django.contrib.auth.models import User
from filmes.models import Filme

class ListarComentarios(LoginRequiredMixin, ListView):
    model = Comentario
    context_object_name = 'comentarios'
    template_name = 'comentarios/comentarios.html'

    def get_queryset(self):
        filme_id = self.kwargs.get('filme_id')
        if filme_id:
            return Comentario.objects.filter(idfilme=filme_id)
        return Comentario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme_id = self.kwargs.get('filme_id')
        if filme_id:
            filme = get_object_or_404(Filme, id=filme_id)
            context['filme'] = filme  # Adiciona o filme ao contexto
        return context     

class CriarComentario(LoginRequiredMixin, CreateView):
    template_name = 'comentarios/addcoment.html'
    form_class = ComentarioForm

    def dispatch(self, request, *args, **kwargs):
        """
        Obtém o filme associado ao comentário.
        """
        self.filme = get_object_or_404(Filme, id=self.kwargs['filme_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Define os valores adicionais para o formulário e salva.
        """
        form.save(user=self.request.user, filme=self.filme)  # Passa o usuário logado e o filme para o método save
        return redirect('comentarios', filme_id=self.filme.id)

    def get_context_data(self, **kwargs):
        """
        Adiciona o filme ao contexto para exibir no template.
        """
        context = super().get_context_data(**kwargs)
        context['filme'] = self.filme
        return context


