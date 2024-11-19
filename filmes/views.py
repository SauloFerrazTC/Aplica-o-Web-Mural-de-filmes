from django.views.generic import View, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.views.generic import ListView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from filmes.models import Filme
from filmes.forms import FilmeForm, FilmeDescricaoForm
from django.contrib.auth.models import User


class ListarFilmes(LoginRequiredMixin, ListView):
    model = Filme
    context_object_name = 'filmes'
    template_name = 'filmes/filmes.html'

    def get_queryset(self):
        """
        Filtra os filmes pela categoria, se a categoria for fornecida na URL.
        Caso contrário, retorna todos os filmes.
        """
        categoria = self.request.GET.get('categoria')  # Obtém a categoria da URL
        if categoria:
            return Filme.objects.filter(categoria=categoria)  # Filtra os filmes pela categoria
        return Filme.objects.all()  # Se não houver categoria, retorna todos os filmes

class FotoFilmes(LoginRequiredMixin, View):

    def get(self, request, arquivo):
        try:
            filme = Filme.objects.get(capa='filmes/fotos/{}' .format(arquivo))
            return FileResponse(filme.capa)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")   
        except Exception as exception:
            raise exception  
            
class CriarFilme(LoginRequiredMixin, CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filmes/cadastroFilme.html'
    success_url = reverse_lazy('listar-filmes')

    def form_valid(self, form):
        form.instance.iduser = self.request.user  # Associa o usuário logado ao campo iduser
        return super().form_valid(form)

class DeletarFilme(LoginRequiredMixin, DeleteView):
    model = Filme
    template_name = 'filmes/deletarfilme.html'
    success_url = reverse_lazy('listar-filmes')

    def get_queryset(self):
        """
        Restringe a exclusão para filmes que pertencem ao usuário logado.
        """
        return Filme.objects.filter(iduser=self.request.user)

class EditarDescricaoFilme(LoginRequiredMixin, UpdateView):
    model = Filme
    form_class = FilmeDescricaoForm  
    template_name = 'filmes/editar.html'
    success_url = reverse_lazy('listar-filmes')

    
    def form_valid(self, form):
        filme = form.save(commit=False)
        filme.save()
        return super().form_valid(form)

    def get_queryset(self):
        """
        Restringe a exclusão para filmes que pertencem ao usuário logado.
        """
        return Filme.objects.filter(iduser=self.request.user)        
