from django import forms
from .models import Categoria, Produto
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['nome_categoria']
        labels={'nome_categoria':'Nome da Categoria'}
        widgets={'nome_categoria':forms.TextInput(attrs={'class':'form-control','placeholder':'Escreva o nome da nova categoria'})}
class ProdutoForm(forms.ModelForm):
    class Meta:
        model=Produto
        fields=['categoria','nome_produto','valor_custo','valor_venda']
        labels={'categoria':'Categoria do Novo Produto','nome_produto':'Nome do Produto','valor_custo':'R$ Custo','valor_venda':'R$ Venda'}
        widgets={'categoria':forms.Select(attrs={'class':'form-select form-select-lg'}),'nome_produto':forms.TextInput(attrs={'class':'form-control','placeholder':'Descreva o nome e especificações do produto'}),'valor_custo':forms.NumberInput(attrs={'class':'form-control','min':'0','step':'0.01'}),'valor_venda':forms.NumberInput(attrs={'class':'form-control','min':'0','step':'0.01'})}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['categoria'].queryset=Categoria.objects.filter(status_cadastro=True)
class EntradaForm(forms.Form):
    produto=forms.ModelChoiceField(queryset=Produto.objects.none(),label='Produto',widget=forms.Select(attrs={'class':'form-select form-select-lg'}))
    quantidade=forms.IntegerField(min_value=1,label='Quantidade',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantos novos produtos?','min':'1'}))
    observacao=forms.CharField(required=False,label='Observação',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Alguma observação para esse item?'}))
    valor_custo=forms.DecimalField(required=False,min_value=0,max_digits=12,decimal_places=2,label='Valor de Custo',widget=forms.NumberInput(attrs={'class':'form-control','min':'0','step':'0.01'}))
    valor_venda=forms.DecimalField(required=False,min_value=0,max_digits=12,decimal_places=2,label='Valor de Venda',widget=forms.NumberInput(attrs={'class':'form-control','min':'0','step':'0.01'}))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['produto'].queryset=Produto.objects.filter(status_cadastro=True)

    def clean_nome_produto(self):
        nome = self.cleaned_data['nome_produto'].strip()
        if not nome:
            raise forms.ValidationError('Informe um nome valido para o produto.')
        return nome
