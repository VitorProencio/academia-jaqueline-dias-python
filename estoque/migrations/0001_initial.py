from decimal import Decimal
from django.db import migrations,models
import django.db.models.deletion
import django.core.validators
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(name='Categoria',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nome_categoria',models.CharField(max_length=150,unique=True)),('status_cadastro',models.BooleanField(default=True))],options={'db_table':'categorias','ordering':['nome_categoria']}),
        migrations.CreateModel(name='Produto',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nome_produto',models.CharField(max_length=200)),('quantidade',models.PositiveIntegerField(default=0)),('observacao',models.TextField(blank=True,default='')),('valor_custo',models.DecimalField(decimal_places=2,default=Decimal('0.00'),max_digits=12,validators=[django.core.validators.MinValueValidator(0)])),('valor_venda',models.DecimalField(decimal_places=2,default=Decimal('0.00'),max_digits=12,validators=[django.core.validators.MinValueValidator(0)])),('status_cadastro',models.BooleanField(default=True)),('categoria',models.ForeignKey(db_column='id_categoria',on_delete=django.db.models.deletion.PROTECT,related_name='produtos',to='estoque.categoria'))],options={'db_table':'produtos','ordering':['nome_produto']})
    ]
