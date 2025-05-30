# estoque/admin.py

from django.contrib import admin
from .models import ItemEstoque, MovimentacaoEstoque

admin.site.register(ItemEstoque)
admin.site.register(MovimentacaoEstoque)
