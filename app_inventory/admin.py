from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Categoria, Produto, LoteProduto, MovimentacaoEstoque


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Administração do modelo Categoria."""
    list_display = ('nome',)  # Exibe apenas o nome da categoria no admin
    search_fields = ('nome',)  # Permite busca pelo nome da categoria


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """Administração do modelo Produto."""
    list_display = ('nome', 'quantidade_estoque', 'categoria', 'fornecedor', 'exibir_imagem', 'preco_venda')
    list_filter = ('categoria', 'fornecedor')  # Permite filtrar por categoria e fornecedor
    search_fields = ('nome', 'categoria__nome', 'fornecedor__nome')  # Busca por nome, categoria e fornecedor
    readonly_fields = ('atualizado_em',)  # Torna a data de atualização apenas leitura

    def exibir_imagem(self, obj):
        """Exibe a imagem do produto no admin."""
        if obj.imagem:  # Verifica se o produto tem imagem associada
            return mark_safe(f'<img src="{obj.imagem.url}" width="50" height="50" />')
        return "Sem Imagem"
    exibir_imagem.short_description = "Imagem"

    def preco_custo_mais_recente(self, obj):
        """Retorna o preço de custo mais recente baseado no lote mais novo."""
        lote_mais_recente = obj.loteproduto_set.order_by('-criado_em').first()
        if lote_mais_recente and lote_mais_recente.preco_custo:
            return f'R$ {lote_mais_recente.preco_custo:.2f}'
        return "Sem preço de custo"
    preco_custo_mais_recente.short_description = "Preço de Custo Mais Recente"


@admin.register(LoteProduto)
class LoteProdutoAdmin(admin.ModelAdmin):
    """Administração do modelo LoteProduto."""
    list_display = ('produto', 'preco_custo', 'numero_lote', 'data_validade', 'criado_em')
    list_filter = ('data_validade', 'criado_em')  # Filtros por data de validade e data de criação
    search_fields = ('produto__nome', 'numero_lote')  # Busca pelo nome do produto e número do lote


@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    """Administração do modelo Movimentação de Estoque."""
    list_display = ('produto', 'quantidade', 'tipo_movimentacao', 'usuario', 'criado_em')
    list_filter = ('tipo_movimentacao', 'produto', 'criado_em')  # Filtra por tipo, produto e data
    search_fields = ('produto__nome', 'usuario__username')  # Busca pelo produto ou usuário
    readonly_fields = ('criado_em',)  # Campo somente leitura
