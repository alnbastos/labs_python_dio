import textwrap

from cadastros import (
    criar_cliente, criar_conta_corrente, listar_contas_corrente
)
from operacoes_bancarias import (
    depositar, sacar, exibir_extrato
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
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    clientes: list[dict] = []
    contas_correntes: list[dict] = []

    while True:

        opcao = menu()

        if opcao == 'nc':
            criar_cliente(clientes)

        elif opcao == 'ncc':
            criar_conta_corrente(AGENCIA, contas_correntes, clientes)

        elif opcao == 'lc':
            listar_contas_corrente(contas_correntes)

        elif opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'q':
            break

        else:
            print(
                'Operação inválida, '
                'por favor selecione novamente a operação desejada.'
            )


main()
