# Controle Financeiro Pessoal

Projeto desenvolvido para a disciplina de Python com o objetivo de praticar conceitos de programação na construção de um sistema simples de controle financeiro.

A ideia foi criar uma aplicação em terminal que permitisse registrar receitas e despesas, visualizar informações salvas e acompanhar o saldo de forma prática.  

## Objetivo do projeto

Este projeto foi desenvolvido para a disciplina de Python com o objetivo de aplicar:

- modularização
- programação orientada a objetos
- persistência de dados em JSON
- validação de entradas
- tratamento de erros
- organização de código seguindo boas práticas

## Funcionalidades

- cadastrar receita ou despesa
- listar todas as transações
- calcular saldo total
- filtrar transações por categoria
- mostrar categorias já utilizadas
- salvar dados automaticamente em arquivo JSON

## Diagrama simples (estrutura do sistema)

```text
Usuário
   ↓
main.py (interface / menu)
   ↓
FinanceiroService (lógica do sistema)
   ↓
Transacao (modelo de dados)
   ↓
Arquivo JSON (persistência)
```

## Estrutura do projeto

```bash
projeto_financeiro_humanizado/
├── main.py
├── models/
│   └── transacao.py
├── services/
│   └── financeiro.py
├── utils/
│   └── validacoes.py
└── data/
    └── transacoes.json
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/henriquematheussilva21-coder/Financeiro_Projeto
```

2. Entre na pasta do projeto:

```bash
cd Financeiro_Projeto
```

3. Execute o arquivo principal:

```bash
python main.py
```

## Exemplo de uso

Ao iniciar o sistema, o menu principal será exibido no terminal:

```text
[1] Adicionar transação
[2] Listar transações
[3] Ver saldo
[4] Filtrar por categoria
[5] Ver categorias
[0] Sair
```

## Decisões tomadas no projeto

- Optei por usar interface em terminal porque a ideia era focar primeiro na lógica do sistema.
- Usei JSON para persistência por ser mais simples de implementar nesta etapa do projeto.
- Separei o código em model, service e utils para evitar misturar responsabilidades e facilitar manutenção.
- Preferi aceitar valor com vírgula porque isso fica mais natural para o usuário brasileiro.

## Validações implementadas

O sistema valida:

- tipo da transação (`receita` ou `despesa`)
- valor maior que zero
- descrição não vazia
- categoria não vazia

## Limitações atuais

- ainda não possui edição ou remoção de transações
- não gera relatório mensal
- não possui gráficos
- não usa banco de dados

## Melhorias futuras

- adicionar edição e exclusão de transações
- gerar relatórios por período
- exportar dados para CSV
- criar uma interface gráfica ou API
- adicionar testes automatizados

## Requisitos atendidos

O projeto atende aos requisitos principais da atividade:

- O sistema deve ser desenvolvido utilizando Python.
- O sistema deve possuir estrutura modular (separação em arquivos).
- O sistema deve utilizar programação orientada a objetos.
- O sistema deve persistir dados em arquivo JSON.
- O sistema deve funcionar via terminal (CLI).
- O sistema deve possuir validação de dados de entrada.
- O sistema deve tratar erros sem interromper a execução.

## Autores

- Matheus Henrique
- Alexandre Tavares
