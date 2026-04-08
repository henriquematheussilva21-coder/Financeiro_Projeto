from services.financeiro import FinanceiroService


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


def main ():
    print("\nBem-vindo ao sistema de controle financeiro.\n")

    while True:
        limpar_tela()
        mostrar_menu()

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            print("  Funcionalidade ainda não implementada.")
        elif opcao == "2":
            print("  Funcionalidade ainda não implementada.")
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