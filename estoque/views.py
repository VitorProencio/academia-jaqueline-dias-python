from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .forms import CategoriaForm,ProdutoForm,EntradaForm
from .models import Produto
@login_required
def dashboard(request):
    produtos=list(Produto.objects.filter(status_cadastro=True).select_related('categoria'))
    context={'produtos':produtos,'total':len(produtos),'em_estoque':sum(p.quantidade>=10 for p in produtos),'estoque_baixo':sum(0<p.quantidade<10 for p in produtos),'sem_estoque':sum(p.quantidade==0 for p in produtos)}
    return render(request,'estoque/dashboard.html',context)
@login_required
def cadastro(request):
    form=ProdutoForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        messages.success(request,'Produto salvo com sucesso!')
        return redirect('dashboard')
    return render(request,'estoque/cadastro.html',{'form':form,'categoria_form':CategoriaForm()})
@login_required
@require_POST
def nova_categoria(request):
    form=CategoriaForm(request.POST)
    if form.is_valid():
        form.save();messages.success(request,'Categoria salva com sucesso!')
    else:
        for errors in form.errors.values():
            for error in errors: messages.error(request,error)
    return redirect('cadastro')
@login_required
def entrada_mercadoria(request):
    form=EntradaForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        with transaction.atomic():
            produto=Produto.objects.select_for_update().get(pk=form.cleaned_data['produto'].pk,status_cadastro=True)
            Produto.objects.filter(pk=produto.pk).update(quantidade=F('quantidade')+form.cleaned_data['quantidade'],observacao=form.cleaned_data['observacao'],**({'valor_custo':form.cleaned_data['valor_custo']} if form.cleaned_data['valor_custo'] is not None else {}),**({'valor_venda':form.cleaned_data['valor_venda']} if form.cleaned_data['valor_venda'] is not None else {}))
        messages.success(request,'Estoque atualizado com sucesso!')
        return redirect('dashboard')
    return render(request,'estoque/entrada.html',{'form':form})
