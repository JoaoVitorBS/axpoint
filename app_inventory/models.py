from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    codigo_barras = models.CharField(max_length=13, unique=True)
    imagem = models.ImageField(upload_to="imagens_produtos/", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    fornecedor = models.ForeignKey(
        "app_suppliers.Fornecedor", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="produtos"
    )
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_validade = models.DateField(blank=True, null=True)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.nome} - {self.codigo_barras}"
