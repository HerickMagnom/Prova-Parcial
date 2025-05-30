# estoque/models.py

from django.db import models

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    codigo_referencia = models.CharField(max_length=50, unique=True)
    localizacao = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField()

    def em_baixo_estoque(self):
        return self.quantidade < self.estoque_minimo

    def __str__(self):
        return self.nome

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    item = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.tipo == 'entrada':
            self.item.quantidade += self.quantidade
        elif self.tipo == 'saida':
            self.item.quantidade -= self.quantidade
        self.item.save()
        super().save(*args, **kwargs)
