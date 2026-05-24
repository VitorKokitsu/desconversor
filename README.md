# Desconversor

API FastAPI para converter payloads de integracao antes do envio ao middleware.

## Requisitos

- Python 3.14
- `uv`
- Acesso ao bucket configurado em `TRANSACTION_BUCKET`
- URL do middleware em `MIDDLEWARE_API_URL` para rotas com envio

## Execucao local

```bash
uv sync
TRANSACTION_BUCKET=nome-do-bucket MIDDLEWARE_API_URL=http://localhost:8000 .venv/bin/python src/main.py
```

## Rotas

- `POST /conversor`: busca o payload no S3 por `transaction_id` e retorna o payload convertido sem enviar ao middleware.
- `POST /conversor/enviar`: busca o payload no S3 por `transaction_id`, converte e envia ao middleware.
- `POST /conversor/payload`: converte um payload informado diretamente no corpo da requisicao.

Exemplo de corpo para rotas que usam S3:

```json
{
  "transaction_id": "transactions/exemplo.json"
}
```
