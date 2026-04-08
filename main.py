from services.financeiro import FinanceiroService
from utils.validacoes import (
    validar_tipo,
    validar_valor,
    validar_descricao,
    validar_categoria,
    CATEGORIAS_PADRAO,
)

# Serviço já carrega o arquivo JSON quando inicia
controle = FinanceiroService()


def limpar_tela():
    print("\n" * 2)


def linha():
    print("-" * 55)


def mostrar_menu():
    linha()
    print("  CONTROLE FINANCEIRO PESSOAL")
    linha()
    print("  [1] Adicionar transação")
    print("  [2] Listar transações")
    print("  [3] Ver saldo")
    print("  [4] Filtrar por categoria")
    print("  [5] Ver categorias")
    print("  [0] Sair")
    linha()


def pedir_dado(mensagem, funcao_validacao):
    while True:
        entrada = input(mensagem)
        try:
            return funcao_validacao(entrada)
        except ValueError as erro:
            print(f"  Erro: {erro}")


def adicionar_transacao():
    print("\nNova transação")
    linha()

    print("  Tipos aceitos: receita ou despesa")
    tipo = pedir_dado("  Tipo: ", validar_tipo)

    descricao = pedir_dado("  Descrição: ", validar_descricao)

    print(f"  Categorias sugeridas: {', '.join(CATEGORIAS_PADRAO)}")
    categoria = pedir_dado("  Categoria: ", validar_categoria)

    valor = pedir_dado("  Valor (R$): ", validar_valor)

    transacao = controle.adicionar_transacao(tipo, descricao, valor, categoria)
    print("\n  Transação cadastrada com sucesso.")
    print(f"  {transacao}")


def listar_transacoes():
    print("\nLista de transações")
    linha()

    transacoes = controle.listar_transacoes()

    if not transacoes:
        print("  Ainda não há transações cadastradas.")
        return

    for transacao in transacoes:
        print(f"  {transacao}")

    print(f"\n  Quantidade total: {len(transacoes)}")


def main():
    print("\nBem-vindo ao sistema de controle financeiro.\n")

    while True:
        limpar_tela()
        mostrar_menu()

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_transacao()
        elif opcao == "2":
            listar_transacoes()
        elif opcao == "3":
            print("  Funcionalidade ainda não implementada.")
        elif opcao == "4":
            print("  Funcionalidade ainda não implementada.")
        elif opcao == "5":
            print("  Funcionalidade ainda não implementada.")
        elif opcao == "0":
            print("\nSaindo...")
            break
        else:
            print("  Opção inválida.")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()