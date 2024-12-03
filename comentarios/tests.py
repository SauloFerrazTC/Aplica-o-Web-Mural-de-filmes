from django.test import TestCase, Client
from django.contrib.auth.models import User
from filmes.models import Filme
from comentarios.models import Comentario
from django.urls import reverse

class ComentarioTests(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.outro_user = User.objects.create_user(username='outro_user', password='12345')
        
        
        self.filme = Filme.objects.create(
            titulo='Filme Teste',
            ano=2024,
            descricao='Descrição do filme',
            categoria='acao',
            iduser=self.user
        )
        
       
        self.comentario = Comentario.objects.create(
            coment='Comentário inicial',
            iduser=self.user,
            idfilme=self.filme
        )
        
        
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_listar_comentarios(self):
        
        response = self.client.get(reverse('listar-comentarios', args=[self.filme.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Comentário inicial')
        
    def test_criar_comentario(self):
        
        data = {'coment': 'Novo comentário'}
        response = self.client.post(reverse('criar-comentarios', args=[self.filme.id]), data)
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Comentario.objects.filter(coment='Novo comentário').exists())

    def test_editar_comentario(self):
   
        data = {'coment': 'Comentário editado'}
        response = self.client.post(reverse('editar-comentarios', args=[self.comentario.id]), data)
        self.assertEqual(response.status_code, 302)  
        self.comentario.refresh_from_db()
        self.assertEqual(self.comentario.coment, 'Comentário editado')

    def test_deletar_comentario(self):
        
        response = self.client.post(reverse('deletar-comentarios', args=[self.comentario.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Comentario.objects.filter(id=self.comentario.id).exists())


