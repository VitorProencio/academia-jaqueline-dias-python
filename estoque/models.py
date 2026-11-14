from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
class Categoria(models.Model):
    nome_categoria=models.CharField(max_length=150,unique=True)
    status_cadastro=models.BooleanField(default=True)
    class Meta:
        db_table='categorias'
        ordering=['nome_categoria']
    def __str__(self): return self.nome_categoria
class Produto(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT,db_column='id_categoria',related_name='produtos')
    nome_produto=models.CharField(max_length=200)
    quantidade=models.PositiveIntegerField(default=0)
    observacao=models.TextField(blank=True,default='')
    valor_custo=models.DecimalField(max_digits=12,decimal_places=2,default=Decimal('0.00'),validators=[MinValueValidator(0)])
    valor_venda=models.DecimalField(max_digits=12,decimal_places=2,default=Decimal('0.00'),validators=[MinValueValidator(0)])
    status_cadastro=models.BooleanField(default=True)
    class Meta:
        db_table='produtos'
        ordering=['nome_produto']
    @property
    def situacao(self):
        if self.quantidade == 0: return 'Sem Estoque!'
        if self.quantidade < 10: return 'Estoque Baixo!'
        return 'Em Estoque!'
    @property
    def classe_status(self):
        if self.quantidade == 0: return 'bg-danger'
        if self.quantidade < 10: return 'bg-warning text-dark'
        return 'bg-success'
    def __str__(self): return self.nome_produto
