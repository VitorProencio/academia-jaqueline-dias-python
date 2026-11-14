from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Categoria,Produto
class EstoqueTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(username='teste',password='senha-segura-123')
        self.client.force_login(self.user)
        self.categoria=Categoria.objects.create(nome_categoria='Collants')
        self.produto=Produto.objects.create(categoria=self.categoria,nome_produto='Collant M',quantidade=8,valor_custo='70.00',valor_venda='110.00')
    def test_status_estoque(self):
        self.assertEqual(self.produto.situacao,'Estoque Baixo!')
        self.produto.quantidade=0
        self.assertEqual(self.produto.situacao,'Sem Estoque!')
        self.produto.quantidade=10
        self.assertEqual(self.produto.situacao,'Em Estoque!')
    def test_dashboard(self):
        response=self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Collant M')
    def test_cadastro_produto(self):
        response=self.client.post(reverse('cadastro'),{'categoria':self.categoria.pk,'nome_produto':'Sapatilha 34-35','valor_custo':'35.00','valor_venda':'60.00'})
        self.assertRedirects(response,reverse('dashboard'))
        self.assertTrue(Produto.objects.filter(nome_produto='Sapatilha 34-35').exists())
    def test_entrada_soma_quantidade(self):
        response=self.client.post(reverse('entrada'),{'produto':self.produto.pk,'quantidade':5,'observacao':'Reposicao'})
        self.assertRedirects(response,reverse('dashboard'))
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade,13)
    def test_entrada_negativa_rejeitada(self):
        response=self.client.post(reverse('entrada'),{'produto':self.produto.pk,'quantidade':-3})
        self.assertEqual(response.status_code,200)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade,8)
    def test_usuario_nao_autenticado_redirecionado(self):
        self.client.logout()
        response=self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code,302)
