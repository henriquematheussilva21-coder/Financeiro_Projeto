# 💰 Financeiro Web

Sistema de controle financeiro pessoal desenvolvido com Flask e SQLite, como projeto da disciplina de Programação de Computadores (P8A - 2026.1).

## 📋 Descrição

Aplicação web para gerenciamento de finanças pessoais, permitindo registrar receitas e despesas, visualizar o saldo atual, acompanhar gastos por categoria e analisar o histórico de transações por meio de gráficos interativos.

Este projeto é uma evolução de um sistema CLI desenvolvido anteriormente em Python, agora com interface web completa, banco de dados relacional e novas funcionalidades como edição, exclusão e dashboard com gráficos.

## 🚀 Funcionalidades

- Cadastrar receitas e despesas
- Listar todas as transações
- Editar e excluir transações
- Calcular saldo, total de receitas e total de despesas
- Filtrar transações por categoria
- Dashboard com gráfico de barras (Receitas vs Despesas)
- Dashboard com gráfico de pizza (Gastos por categoria)

## 🛠️ Tecnologias

- Python 3.13
- Flask 3.1
- Flask-SQLAlchemy 3.1
- SQLite
- HTML5 + CSS3
- Chart.js 4.4

## 📁 Estrutura do Projeto
```text
financeiro-web/
├── app.py                  # Rotas e configuração do Flask
├── database.py             # Instância do SQLAlchemy
├── requirements.txt        # Dependências do projeto
├── models/
│   └── transacao.py        # Modelo de dados
├── services/
│   └── financeiro.py       # Regras de negócio
├── utils/
│   └── validacoes.py       # Validações de entrada
├── templates/
│   ├── base.html           # Template base com navbar
│   ├── index.html          # Dashboard principal
│   ├── transacoes.html     # Listagem de transações
│   └── form_transacao.html # Formulário de cadastro/edição
├── static/
│   └── style.css           # Estilização da interface
└── data/
    └── financeiro.db       # Banco de dados SQLite (gerado automaticamente)
```

## ⚙️ Como executar

**1. Clone o repositório:**
```bash
git clone https://github.com/henriquematheussilva21-coder/financeiro-web.git
cd financeiro-web
```

**2. Configure a versão do Python:**
```bash
pyenv local 3.13.0
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Execute a aplicação:**
```bash
python app.py
```

**5. Acesse no navegador:**
```bash
http://127.0.0.1:5000
```

## 🗄️ Diagrama do Banco de Dados

```text
┌─────────────────────────┐
│        transacoes       │
├─────────────────────────┤
│ id          INTEGER (PK)│
│ tipo        STRING(10)  │
│ descricao   STRING(100) │
│ valor       FLOAT       │
│ categoria   STRING(50)  │
│ data        STRING(10)  │
└─────────────────────────┘
```

## 📌 Casos de Uso Principais

- **Registrar transação:** usuário preenche tipo, descrição, valor e categoria
- **Visualizar dashboard:** sistema exibe saldo, gráficos e últimas transações
- **Filtrar por categoria:** usuário seleciona uma categoria e visualiza apenas suas transações
- **Editar transação:** usuário altera os dados de uma transação existente
- **Excluir transação:** usuário remove uma transação com confirmação

## 👤 Autor

**Matheus Henrique dos Santos Silva**  
Disciplina: Programação de Computadores — P8A (2026.1)
