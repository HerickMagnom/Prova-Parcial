# estoque/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('novo-item/', views.cadastrar_item, name='cadastrar_item'),
    path('movimentar/', views.movimentar_estoque, name='movimentar_estoque'),
    path('remover/<int:item_id>/', views.remover_item, name='remover_item'),
]
