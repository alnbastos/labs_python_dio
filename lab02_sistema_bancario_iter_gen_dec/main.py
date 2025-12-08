import textwrap

from cliente import PessoaFisica
from conta_corrente import ContaCorrente
from cadastro import (
    listar_contas_corrente,
    criar_cliente, criar_conta_corrente,
)
from transacao import (
    depositar, sacar, exibir_extrato,
)


def menu():
    menu = '''
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNovo cliente
    [ncc]\tNova conta corrente
    [lc]\tListar conta corrente

    [q]\tSair

    => '''
    return input(textwrap.dedent(menu))


def main():
    clientes: list[PessoaFisica] = []
    contas_correntes: list[ContaCorrente] = []

    while True:

        opcao = menu()

        if opcao == 'd':
            depositar(clientes)

        elif opcao == 's':
            sacar(clientes)

        elif opcao == 'e':
            exibir_extrato(clientes)

        elif opcao == 'nc':
            criar_cliente(clientes)

        elif opcao == 'ncc':
            numero_conta = len(contas_correntes) + 1
            criar_conta_corrente(numero_conta, contas_correntes, clientes)

        elif opcao == 'lc':
            listar_contas_corrente(contas_correntes)

        elif opcao == 'q':
            break

        else:
            print(
                '\n@@@ Operação inválida, por favor selecione '
                'novamente a operação desejada. @@@'
            )


main()
