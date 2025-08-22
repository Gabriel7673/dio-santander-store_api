# Dio Santander Store API

Uma API RESTful para gerenciamento de produtos de uma loja, desenvolvida com FastAPI, MongoDB e Pydantic.

## Funcionalidades

- CRUD para produtos
- Filtros por preço mínimo/máximo
- Validação de dados com Pydantic
- Testes automatizados com Pytest e Pytest-Asyncio
- Integração com MongoDB via Motor

## Requisitos

- Python >= 3.13.1
- MongoDB (pode ser iniciado via Docker)
- Poetry

## Estrutura do Projeto
```
dio_santander_store_api/
  controllers/   # Rotas e endpoints
  core/          # Configurações e exceções
  db/            # Conexão com banco de dados
  models/        # Modelos de dados
  schemas/       # Schemas Pydantic
  usecases/      # Regras de negócio
  utils/         # Utilitários
tests/           # Testes automatizados
```

## Instalação

```sh
poetry install
```

## Configuração
Crie um arquivo .env na raiz do projeto com a variável:
```
DATABASE_URL = "mongodb://localhost:27017/store?uuidRepresentation=standard"
```

## Executando o MongoDB com Docker
```
docker-compose up -d
```

## Rodando a aplicação
```
make run
```

## Testes
```
make test
```

A documentação automática pode ser acessada em http://localhost:8000/docs.

Desenvolvido como projeto de programação para construção de API simples no Bootcamp Santander Python 2025.
