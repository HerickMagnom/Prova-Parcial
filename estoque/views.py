# estoque/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemEstoque
from .forms import ItemEstoqueForm, MovimentacaoEstoqueForm

def dashboard(request):
    itens = ItemEstoque.objects.all()
    return render(request, 'estoque/dashboard.html', {'itens': itens})

def cadastrar_item(request):
    form = ItemEstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'estoque/cadastro_item.html', {'form': form})

def movimentar_estoque(request):
    form = MovimentacaoEstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'estoque/movimentacao.html', {'form': form})

def remover_item(request, item_id):
    item = get_object_or_404(ItemEstoque, id=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('dashboard')
