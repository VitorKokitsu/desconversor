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
API_KEY=chave-local TRANSACTION_BUCKET=nome-do-bucket TRANSACTION_BUCKET_DEMO=nome-do-bucket-demo MIDDLEWARE_API_URL=http://localhost:8000 .venv/bin/python src/main.py
```

## Rotas

Todas as rotas de conversao exigem o header `X-API-Key` com o valor de `API_KEY`. `GET /healthcheck` responde `204` sem autenticacao.


- `POST /conversor`: busca o payload no S3 por `transaction_id` e retorna o payload convertido sem enviar ao middleware.
- `POST /conversor/enviar`: busca o payload no S3 por `transaction_id`, converte e envia ao middleware.
- `POST /conversor/payload`: converte um payload informado diretamente no corpo da requisicao.
- `POST /conversor/payload/enviar`: converte um payload informado diretamente no corpo da requisicao e envia ao middleware.

As rotas de envio aceitam o query param `nome_config` (nome da configuracao no middleware), obrigatorio para processos do PedPreco (ingestao, autenticacao e retorno), cujas rotas no middleware exigem esse valor e ele nao vem no payload do Protheus. Exemplo: `POST /conversor/enviar?nome_config=nome-da-config`.

Exemplo de corpo para rotas que usam S3:

```json
{
  "transaction_id": "transactions/exemplo.json"
}
```

## Deploy

Producao: `https://desconversor.cotefacil.net` (ECS Fargate no cluster `desconversor`, atras do ALB `lb-internal-prod`).

- `infra/global`: repositorio ECR, cluster ECS e log group.
- `infra/prod`: target group, regra do listener por host, security group, task definition e servico.
- Push na `main` executa `.github/workflows/deploy-prod.yml`: aplica o Terraform, publica a imagem `desconversor:prod` no ECR e forca um novo deploy do servico.

Antes do primeiro deploy, criar o segredo `prod/desconversor` no Secrets Manager com as chaves `api_key`, `middleware_api_url`, `transaction_bucket` e `transaction_bucket_demo`.

