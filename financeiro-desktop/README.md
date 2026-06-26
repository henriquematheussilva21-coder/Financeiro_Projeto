# 💰 Financeiro Desktop

Sistema de controle financeiro pessoal desenvolvido com Python e Tkinter, como projeto da disciplina de Programação de Computadores (P8A - 2026.1).

## 📋 Descrição

Aplicação desktop para gerenciamento de finanças pessoais, permitindo registrar receitas e despesas, visualizar o saldo atual, acompanhar gastos por categoria e gerenciar o histórico de transações por meio de uma interface gráfica nativa.

Este projeto é a versão desktop do sistema [Financeiro Web](../financeiro-web), reaproveitando toda a camada de lógica de negócio e banco de dados, substituindo apenas a interface web por uma interface gráfica com Tkinter.

## 🚀 Funcionalidades

- Dashboard com cards de receitas, despesas e saldo atual
- Cadastrar receitas e despesas
- Listar todas as transações
- Editar e excluir transações
- Filtrar transações por categoria
- Banco de dados SQLite persistente

## 🛠️ Tecnologias

- Python 3.13
- Tkinter (interface gráfica nativa)
- SQLAlchemy 2.0
- SQLite

## 📁 Estrutura do Projeto
## 📂 Estrutura do Projeto (Desktop)

```text
financeiro-desktop/
├── main.py                 # Interface gráfica e navegação
├── database.py             # Configuração do SQLAlchemy
├── requirements.txt        # Dependências do projeto
├── models/
│   └── transacao.py        # Modelo de dados
├── services/
│   └── financeiro.py       # Regras de negócio
├── utils/
│   └── validacoes.py       # Validações de entrada
└── data/
    └── financeiro.db       # Banco de dados SQLite (gerado automaticamente)
```

## ⚙️ Como executar

**1. Clone o repositório:**
```bash
git clone https://github.com/henriquematheussilva21-coder/Financeiro_Projeto.git
cd Financeiro_Projeto/financeiro-desktop
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
python main.py
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

- **Registrar transação:** usuário preenche tipo, descrição, valor e categoria em janela modal
- **Visualizar dashboard:** sistema exibe saldo, cards coloridos e últimas transações
- **Filtrar por categoria:** usuário seleciona uma categoria e visualiza apenas suas transações
- **Editar transação:** usuário seleciona uma linha da tabela e edita os dados
- **Excluir transação:** usuário seleciona uma linha e confirma a exclusão

## 👤 Autor

**Matheus Henrique dos Santos Silva**

## 🎓 Informações Acadêmicas

- **Disciplina:** Programação de Computadores
- **Professor:** Edkallenn Silva De Lima
- **Período:** P8A — 2026.1