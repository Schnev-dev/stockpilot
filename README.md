# StockPilot — API de Gerenciamento de Estoque

StockPilot é uma API REST desenvolvida com **Python e FastAPI** para realizar operações de gerenciamento de produtos em estoque.

O projeto utiliza **Poetry** para o gerenciamento de dependências e **Docker/Podman** para a conteinerização da aplicação.

## Tecnologias utilizadas

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- Poetry
- Docker / Podman
- Docker Compose / Podman Compose

## Funcionalidades

A API permite:

- Cadastrar novos produtos.
- Listar todos os produtos.
- Consultar produtos por ID.
- Atualizar parcialmente os dados de um produto.
- Excluir produtos do estoque.
- Validar os dados recebidos utilizando Pydantic.

Cada produto possui `nome`, `preco`, `quantidade` e `minimo_estoque`.

## Estrutura do projeto

```text
stockpilot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── servico.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Pré-requisitos

Para executar a aplicação, é necessário ter instalado:

- Git
- Docker com Docker Compose, ou Podman com um provedor Compose funcional

Não é necessário instalar manualmente as dependências Python no computador, pois elas são instaladas durante a construção da imagem Docker.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Schnev-dev/stockpilot.git
cd stockpilot
```

### 2. Construir e iniciar os contêineres

Com Docker Compose:

```bash
docker compose up --build -d
```

No Windows, utilizando o módulo Python do Podman Compose:

```powershell
py -m podman_compose up --build -d
```

### 3. Acessar a aplicação e a documentação

Após iniciar a aplicação, acesse:

http://localhost:8085/docs

A documentação interativa é disponibilizada pelo Swagger UI.

### 4. Encerrar a aplicação

Com Docker Compose:

```
docker compose down
```

Com Podman Compose:

```powershell
py -m podman_compose down
```

## Endpoints disponíveis

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verificação do status da API |
| POST | `/produtos` | Cadastrar novo produto |
| GET | `/produtos` | Listar todos os produtos |
| GET | `/produtos/{produto_id}` | Consultar produto por ID |
| PATCH | `/produtos/{produto_id}` | Atualizar dados do produto |
| DELETE | `/produtos/{produto_id}` | Excluir produto do estoque |

## Exemplo de cadastro

Requisição:

```http
POST /produtos
Content-Type: application/json
```

```json
{
  "nome": "Teclado Mecânico",
  "preco": 120.0,
  "quantidade": 15,
  "minimo_estoque": 5
}
```

Resposta esperada:

```json
{
  "id": 1,
  "nome": "Teclado Mecânico",
  "preco": 120.0,
  "quantidade": 15,
  "minimo_estoque": 5
}
```

Código HTTP: `201 Created`.

## Variáveis de ambiente

O serviço utiliza a variável `ENVIRONMENT`, definida no arquivo `docker-compose.yml` com o valor `development`.

## Persistência de dados

Atualmente, os produtos são armazenados em um dicionário Python na memória.

Os dados podem ser perdidos quando o processo da aplicação é reiniciado. Uma versão futura poderá utilizar PostgreSQL para persistência.

## Testes realizados

As operações CRUD foram testadas por meio do Swagger UI (`/docs`), incluindo:

- Cadastro de produtos — HTTP 201.
- Consulta de produtos — HTTP 200.
- Produto inexistente — HTTP 404.
- Dados inválidos — HTTP 422.
- Atualização parcial de produtos — HTTP 200.
- Exclusão de produtos — HTTP 204.

## Autor

Desenvolvido por **Schnev-dev** ([schnevthompson@proton.me](mailto:schnevthompson@proton.me)) como atividade prática, com foco em Python, FastAPI, Poetry e conteinerização.

