# Create your views here.
from django.views.generic import View, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import FileResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from comentarios.models import Comentario
from .forms import ComentarioForm, EditarComentarioForm
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
        return redirect('listar-comentarios', filme_id=self.filme.id)

    def get_context_data(self, **kwargs):
        """
        Adiciona o filme ao contexto para exibir no template.
        """
        context = super().get_context_data(**kwargs)
        context['filme'] = self.filme
        return context


class DeletarComentarios(LoginRequiredMixin, DeleteView):

    model = Comentario
    template_name = 'comentarios/deletarcoment.html'
    
    def get_success_url(self):
        return reverse_lazy('listar-comentarios', args=[self.object.idfilme.id])    

    def get_queryset(self):
        """
        Restringe a exclusão para comentarios que pertencem ao usuário logado.
        """
        return Comentario.objects.filter(iduser=self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER', reverse('listar-comentarios', args=[self.object.idfilme.id]))
        return context       

class EditarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = EditarComentarioForm
    template_name = 'comentarios/editcoment.html'

    def get_success_url(self):
        return reverse_lazy('listar-comentarios', args=[self.object.idfilme.id])     

    def get_object(self, queryset=None):
        # Obtém o comentário com base no ID fornecido na URL
        return get_object_or_404(Comentario, pk=self.kwargs['pk'])

    def form_valid(self, form):
        # Salva a atualização do comentário
        form.save()
        return super().form_valid(form)


    def get_queryset(self):
        """
        Restringe a exclusão para filmes que pertencem ao usuário logado.
        """
        return Comentario.objects.filter(iduser=self.request.user)       