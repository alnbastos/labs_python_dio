from abc import ABC, abstractclassmethod, abstractproperty

from conta_corrente import Conta
from utils import log_transacao, filtrar_cliente, recuperar_conta_cliente


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


@log_transacao
def depositar(clientes: list) -> None:
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Operação falhou! Cliente não encontrado. @@@')
        return 'FALHA: Cliente não encontrado.'

    numero_conta = 0
    if len(cliente.contas) > 1:
        numero_conta = \
            int(input('Informe o número da conta que deseja depositar: ')) - 1

    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente, numero_conta)
    if not conta:
        return 'FALHA: Cliente não possui conta.'

    cliente.realizar_transacao(conta, transacao)
    return 'SUCESSO'


@log_transacao
def sacar(clientes: list) -> None:
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Operação falhou! Cliente não encontrado. @@@')
        return

    numero_conta = 0
    if len(cliente.contas) > 1:
        numero_conta = \
            int(input('Informe o número da conta que deseja sacar: ')) - 1

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente, numero_conta)
    if not conta:
        return 'FALHA: Cliente não encontrado.'

    cliente.realizar_transacao(conta, transacao)
    return 'SUCESSO'


@log_transacao
def exibir_extrato(clientes: list) -> None:
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Operação falhou! Cliente não encontrado. @@@')
        return 'FALHA: Cliente não encontrado.'

    numero_conta = 0
    if len(cliente.contas) > 1:
        numero_conta = int(input(
            'Informe o número da conta que deseja visualizar extrato: '
        )) - 1

    conta = recuperar_conta_cliente(cliente, numero_conta)
    if not conta:
        return

    print('\n================ EXTRATO ================')
    tipo_extrato = input('Informe o tipo de operação que deseja visualizar: ')
    transacoes = conta.historico.gerar_relatorio(tipo_extrato)

    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in transacoes:
            extrato += (
                f"\n{transacao['data']}\n{transacao['tipo']}:"
                f"\n\tR$ {transacao['valor']:.2f}"
            )

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('==========================================')
