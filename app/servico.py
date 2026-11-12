from app.schemas import ProdutoCriar, ProdutoAtualizar

produtos = {}
next_id = 1

def criar_produto(produto: ProdutoCriar):
    """Cria um novo produto e o adiciona ao estoque."""

    global next_id

    novo_produto = {
        "id": next_id,
        **produto.model_dump()
    }
    produtos[next_id] = novo_produto
    next_id += 1
    return novo_produto


def listar_produtos():
    """Retorna a lista de todos os produtos no estoque."""
    return list(produtos.values())

def obter_produto(produto_id: int):
    """Retorna um produto específico pelo seu ID."""
    return produtos.get(produto_id)


def atualizar_produto(produto_id: int, produto_atualizado: ProdutoAtualizar):
    """Atualiza os detalhes de um produto existente."""
    produto = produtos.get(produto_id)
    if produto is None:
        return None

    update_data = produto_atualizado.model_dump(exclude_unset=True, exclude_none=True)
    if not update_data:
        raise ValueError("Nenhum campo válido para atualização foi fornecido.")
    produto.update(update_data)
    return produto

def deletar_produto(produto_id: int):
    """Deleta um produto específico pelo seu ID."""
    produto = produtos.pop(produto_id, None)
    return produto