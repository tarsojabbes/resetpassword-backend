# Reset Password LDAP LCC - Backend

## Importante

- É necessário um arquivo .env com uma variável "KEY". Ela vai ser usada por questões de segurança. Então na requisição, inclua um campo "key" no JSON do corpo da requisição.

## Run

Para rodar a aplicação e instalar as dependências

```sh
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --port 5000
```

Copie o `.env.sample` para o `.env` configurando suas variáveis de ambiente:

```sh
cp .env.sample .env
```

### Com Docker

#### Pré-requisitos

- Docker

1. Faça o build da imagem:

```sh
make build
```

2. Rode o container:

```sh
make run # rodar em foreground
# or
make rund # rodar em background
```

3. Parar o container (background) após o uso:

```sh
make stop
```
