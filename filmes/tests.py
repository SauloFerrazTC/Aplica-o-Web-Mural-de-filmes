from django.test import TestCase, Client
from django.contrib.auth.models import User
from filmes.models import Filme
from django.urls import reverse

class FilmeTests(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        
        self.filme = Filme.objects.create(
            titulo='Filme de Teste',
            ano=2024,
            descricao='Descrição de Teste',
            capa=None,
            categoria='acao',
            iduser=self.user
        )
        
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_listar_filmes(self):
        response = self.client.get(reverse('listar-filmes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Filme de Teste')
        
    def test_criar_filme(self):
        data = {
            'titulo': 'Novo Filme',
            'ano': 2025,
            'descricao': 'Descrição do novo filme',
            'categoria': 'comedia',
        }
        response = self.client.post(reverse('criar-filmes'), data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Filme.objects.filter(titulo='Novo Filme').exists())

    def test_editar_descricao_filme(self):
        data = {
            'descricao': 'Descrição atualizada',
        }
        response = self.client.post(reverse('editar-filmes', args=[self.filme.id]), data)
        self.assertEqual(response.status_code, 302)  
        self.filme.refresh_from_db()
        self.assertEqual(self.filme.descricao, 'Descrição atualizada')
        
    def test_deletar_filme(self):
        response = self.client.post(reverse('deletar-filmes', args=[self.filme.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Filme.objects.filter(id=self.filme.id).exists())

    def test_foto_filme(self):

        response = self.client.get(reverse('foto-filmes', args=['foto_nao_existente.jpg']))
        self.assertEqual(response.status_code, 404)  
