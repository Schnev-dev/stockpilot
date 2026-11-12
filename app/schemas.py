from pydantic import BaseModel, Field


class ProdutoCriar(BaseModel):
    nome: str
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)
    minimo_estoque: int = Field(ge=0)

class ProdutoAtualizar(BaseModel):
    nome: str | None = None
    preco: float | None = Field(default=None, gt=0)
    quantidade: int | None = Field(default=None, ge=0)
    minimo_estoque: int | None = Field(default=None, ge=0)