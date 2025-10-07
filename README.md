# Fast Zero

Uma aplicação de gerenciamento de tarefas (todos) construída com FastAPI, oferecendo um sistema completo de autenticação e CRUD para usuários e tarefas.

## 🚀 Características

- **API RESTful** construída com FastAPI
- **Autenticação JWT** com OAuth2
- **Sistema de usuários** com registro, login e gerenciamento de perfis
- **Gerenciamento de tarefas** com estados (draft, todo, doing, done, trash)
- **Banco de dados** PostgreSQL com SQLAlchemy ORM
- **Migrações** automatizadas com Alembic
- **Testes** abrangentes com pytest
- **Containerização** com Docker
- **Linting e formatação** com Ruff
- **Cobertura de testes** com pytest-cov

## 🛠️ Tecnologias

- **Python 3.13+**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Banco de dados relacional
- **Alembic** - Migrações de banco de dados
- **JWT** - Autenticação baseada em tokens
- **Pydantic** - Validação de dados
- **Docker** - Containerização
- **pytest** - Framework de testes
- **Ruff** - Linter e formatador

## 📋 Pré-requisitos

- Python 3.13 ou superior
- Docker e Docker Compose (opcional)
- PostgreSQL (se não usar Docker)

## 🚀 Instalação e Execução

### Método 1: Usando Docker (Recomendado)

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd fast_zero
```

2. **Crie o arquivo `.env`:**
```bash
# Database
DATABASE_URL=postgresql://postgres:postgres@fastzero_database:5432/fastzero

# JWT
SECRET_KEY=sua-chave-secreta-super-segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

3. **Execute com Docker Compose:**
```bash
docker-compose up --build
```

A aplicação estará disponível em `http://localhost:8000`

### Método 2: Execução Local

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd fast_zero
```

2. **Instale as dependências:**
```bash
pip install poetry
poetry install
```

3. **Configure o ambiente:**
```bash
# Crie um arquivo .env com as variáveis necessárias
DATABASE_URL=postgresql://usuario:senha@localhost:5432/fastzero
SECRET_KEY=sua-chave-secreta-super-segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. **Execute as migrações:**
```bash
poetry run alembic upgrade head
```

5. **Execute a aplicação:**
```bash
poetry run task run
```

## 📚 API Endpoints

### Autenticação (`/auth`)

- `POST /auth/token` - Login e obtenção de token JWT
- `POST /auth/refresh_token` - Renovação do token

### Usuários (`/users`)

- `POST /users/` - Criar novo usuário
- `GET /users/` - Listar usuários (com paginação)
- `GET /users/{user_id}` - Obter usuário por ID
- `PUT /users/{user_id}` - Atualizar usuário
- `DELETE /users/{user_id}` - Deletar usuário

### Tarefas (`/todos`)

- `POST /todos/` - Criar nova tarefa
- `GET /todos/` - Listar tarefas do usuário (com filtros)
- `PATCH /todos/{todo_id}` - Atualizar tarefa
- `DELETE /todos/{todo_id}` - Deletar tarefa

## 🔐 Autenticação

A aplicação usa autenticação JWT (JSON Web Token). Para acessar endpoints protegidos:

1. Faça login em `/auth/token` com email e senha
2. Use o token retornado no header `Authorization: Bearer <token>`

## 📊 Estados das Tarefas

As tarefas podem ter os seguintes estados:
- `draft` - Rascunho
- `todo` - Para fazer
- `doing` - Em andamento
- `done` - Concluída
- `trash` - Lixeira

## 🧪 Testes

Execute os testes com:
```bash
poetry run task test
```

Para executar apenas os testes:
```bash
poetry run pytest
```

Para ver a cobertura de testes:
```bash
poetry run task test
# O relatório HTML será gerado em htmlcov/
```

## 🔧 Comandos Disponíveis

```bash
# Executar aplicação
poetry run task run

# Executar testes
poetry run task test

# Linting
poetry run task lint

# Formatação
poetry run task format

# Pré-formatação (fix automático)
poetry run task pre_format

# Pré-teste (lint + testes)
poetry run task pre_test

# Pós-teste (gera relatório de cobertura)
poetry run task post_test
```

## 📁 Estrutura do Projeto

```
fast_zero/
├── fast_zero/
│   ├── __init__.py
│   ├── app.py              # Aplicação principal
│   ├── database.py         # Configuração do banco
│   ├── models.py           # Modelos SQLAlchemy
│   ├── schemas.py          # Schemas Pydantic
│   ├── security.py         # Utilitários de segurança
│   ├── settings.py         # Configurações
│   └── routers/
│       ├── auth.py         # Rotas de autenticação
│       ├── todos.py        # Rotas de tarefas
│       └── users.py        # Rotas de usuários
├── tests/                  # Testes
├── migrations/             # Migrações Alembic
├── compose.yaml           # Docker Compose
├── dockerfile             # Dockerfile
├── pyproject.toml         # Configurações do projeto
└── README.md
```

## 🌐 Documentação da API

Após iniciar a aplicação, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔄 Migrações

Para criar uma nova migração:
```bash
poetry run alembic revision --autogenerate -m "Descrição da migração"
```

Para aplicar migrações:
```bash
poetry run alembic upgrade head
```

## 🐳 Docker

### Build da imagem:
```bash
docker build -t fastzero_app .
```

### Executar container:
```bash
docker run -p 8000:8000 fastzero_app
```

## 📝 Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|---------|
| `DATABASE_URL` | URL de conexão com o banco | - |
| `SECRET_KEY` | Chave secreta para JWT | - |
| `ALGORITHM` | Algoritmo de assinatura JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tempo de expiração do token | `30` |

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Diego Canafistula**
- Email: diego.canafistula@gmail.com

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas, por favor abra uma issue no repositório.
