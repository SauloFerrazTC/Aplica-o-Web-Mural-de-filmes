from django.views.generic import View, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.views.generic import ListView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from filmes.models import Filme
from filmes.serializers import FilmeSerializer, FilmeDescricaoSerializer, CriarFilmeSerializer
from filmes.forms import FilmeForm, FilmeDescricaoForm
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


class ListarFilmes(LoginRequiredMixin, ListView):
    model = Filme
    context_object_name = 'filmes'
    template_name = 'filmes/filmes.html'

    def get_queryset(self):

        categoria = self.request.GET.get('categoria')  # Obtém a categoria da URL
        if categoria:
            return Filme.objects.filter(categoria=categoria)  
        return Filme.objects.all()  

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
        form.instance.iduser = self.request.user  
        return super().form_valid(form)

class DeletarFilme(LoginRequiredMixin, DeleteView):
    model = Filme
    template_name = 'filmes/deletarfilme.html'
    success_url = reverse_lazy('listar-filmes')

    def get_queryset(self):

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

        return Filme.objects.filter(iduser=self.request.user)  




class ListarFilmesAPI(ListAPIView):

    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = [IsAuthenticated]  
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        categoria = self.request.query_params.get('categoria')
        if categoria:
            return Filme.objects.filter(categoria=categoria)
        return Filme.objects.all()  

class APIDeletarFilmes(DestroyAPIView):
    serializer_class = FilmeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Filme.objects.filter(iduser=self.request.user)  

    def perform_destroy(self, instance):
        instance.delete()

class EditarAPIDescricaoFilme(UpdateAPIView):

    queryset = Filme.objects.all()  
    serializer_class = FilmeDescricaoSerializer  
    permission_classes = [permissions.IsAuthenticated]


class CriarFilmeAPI(CreateAPIView):
    queryset = Filme.objects.all()  
    serializer_class = CriarFilmeSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(iduser=self.request.user)
