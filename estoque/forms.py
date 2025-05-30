# estoque/forms.py

from django import forms
from .models import ItemEstoque, MovimentacaoEstoque

class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = '__all__'

class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['item', 'tipo', 'quantidade']
