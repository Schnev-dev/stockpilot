from fastapi import FastAPI, HTTPException, Response, status
from app.servico import criar_produto, listar_produtos, obter_produto, atualizar_produto, deletar_produto
from app.schemas import ProdutoCriar, ProdutoAtualizar


app = FastAPI(title="StockPilot", description="API para gerenciamento de estoque", version="1.0.0")

@app.get("/")
def raiz():
    return {"message": "StockPilot API está ativa", "docs": "/docs"}

@app.post("/produtos", status_code=201)
def criar_produto_endpoint(produto: ProdutoCriar):
    """
    Endpoint para criar um novo produto.
    """
    return criar_produto(produto)

@app.get("/produtos", status_code=200)
def listar_produtos_endpoint():
    """
    Endpoint para listar todos os produtos.
    """
    return listar_produtos()

@app.get("/produtos/{produto_id}")
def obter_produto_endpoint(produto_id: int):
    """
    Endpoint para obter um produto específico pelo seu ID.
    """
    produto = obter_produto(produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.patch("/produtos/{produto_id}")
def atualizar_produto_endpoint(produto_id: int, produto_atualizado: ProdutoAtualizar):
    """
    Endpoint para atualizar os detalhes de um produto existente.
    """
    produto = atualizar_produto(produto_id, produto_atualizado)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto_endpoint(produto_id: int):
    """
    Endpoint para deletar um produto específico pelo seu ID.
    """
    produto = deletar_produto(produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return Response(status_code=204)