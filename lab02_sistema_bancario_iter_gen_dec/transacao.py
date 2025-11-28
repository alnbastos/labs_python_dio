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
        return

    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes: list) -> None:
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Operação falhou! Cliente não encontrado. @@@')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes: list) -> None:
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Operação falhou! Cliente não encontrado. @@@')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print('\n================ EXTRATO ================')
    # TODO: atualizar a implementação para utilizar
    # o gerador definido em Historico
    transcoes = conta.historico.transacoes

    extrato = ''
    if not transcoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in transcoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('==========================================')
