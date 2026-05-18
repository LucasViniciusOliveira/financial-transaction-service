# Fast API Project 🚀

Projeto criado para estudos da linguagem Python utilizando o framework FastAPI.

O objetivo deste projeto é aprender conceitos importantes do ecossistema Python, como:

- Criação de APIs com FastAPI
- Gerenciamento de dependências
- Utilização de ambientes virtuais (`venv`)
- Organização de projetos Python
- Execução de aplicações no WSL/Linux
- Boas práticas de desenvolvimento

---

# 📦 Configuração do Ambiente

## Atualizar dependências do sistema

```bash
sudo apt update
```

---

## Instalar suporte ao ambiente virtual no WSL

```bash
sudo apt install python3.12-venv
```

> Caso utilize outra versão do Python, altere a versão no comando acima.

---

# 🐍 Ambiente Virtual

## Criar ambiente virtual

```bash
python3 -m venv venv
```

---

## Ativar ambiente virtual

```bash
source venv/bin/activate
```

Após ativar, o terminal ficará parecido com:

```bash
(venv) lucas@DESKTOP
```

---

# 📚 Instalação de Dependências

## Instalar bibliotecas no ambiente virtual

```bash
pip install fastapi uvicorn
```

---

## Atualizar arquivo de dependências

```bash
pip freeze > requirements.txt
```

---

## Instalar dependências utilizando o arquivo requirements.txt

```bash
pip install -r requirements.txt
```

---

# ▶️ Executar Projeto

Exemplo para iniciar uma aplicação FastAPI:

```bash
uvicorn main:app --reload
```

---

# 📁 Estrutura Inicial do Projeto

```txt
fast-api-project/
│
├── venv/
├── main.py
├── requirements.txt
└── README.md
```

---

# ✅ Boas práticas

Adicionar o ambiente virtual no `.gitignore`:

```gitignore
venv/
__pycache__/
```

Isso evita enviar arquivos desnecessários para o repositório.


pip install sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

Gerar migrations:
alembic revision --autogenerate -m "Initial Migration"

Executar as migration criadas:
alembic upgrade head