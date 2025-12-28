import textwrap

from cliente import criar_cliente
from conta import criar_conta_corrente, listar_contas_corrente
from transacao import depositar, sacar, exibir_extrato


def menu():
    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNovo cliente
    [ncc]\tNova conta corrente
    [lc]\tListar conta corrente

    [q]\tSair

    => """
    return input(textwrap.dedent(menu))


def main():
    clientes = []
    contas_correntes = []

    while True:

        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nc":
            criar_cliente(clientes)

        elif opcao == "ncc":
            criar_conta_corrente(contas_correntes, clientes)

        elif opcao == "lc":
            listar_contas_corrente(contas_correntes)

        elif opcao == "q":
            break

        else:
            print(
                "\n@@@ Operação inválida, por favor selecione "
                "novamente a operação desejada. @@@"
            )


main()
