from django.views.generic import View, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.views.generic import ListView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from filmes.models import Filme
from filmes.forms import FilmeForm


class ListarFilmes(LoginRequiredMixin, ListView):

    model = Filme
    context_object_name = 'filmes'
    template_name = 'filmes/filmes.html'

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