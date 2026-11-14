from django.contrib import admin
from .models import Categoria,Produto
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('id','nome_categoria','status_cadastro')
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','nome_produto','categoria','quantidade','valor_venda','status_cadastro')
    list_filter=('categoria','status_cadastro')
