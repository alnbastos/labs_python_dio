from abc import ABC, abstractmethod
from datetime import datetime
from utils import filtrar_cliente, recuperar_conta_cliente


class Transacao(ABC):
    @abstractmethod
    def registrar(conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self._valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes: list[dict] = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S'),
        })


def depositar(clientes: list[object]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        print("\n@@@ Operação falhou! Cliente não encontrado. @@@")
        return

    numero_conta = 0
    if len(cliente.contas) > 1:
        numero_conta = \
            int(input('Informe o número da conta que deseja depositar: '))

    conta = recuperar_conta_cliente(cliente, numero_conta)
    valor = float(input('Informe o valor do depósito: '))
    cliente.realizar_transacao(conta, transacao=Deposito(valor))


def sacar(clientes: list[object]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        print("\n@@@ Operação falhou! Cliente não encontrado. @@@")
        return

    numero_conta = 0
    if len(cliente.contas) > 1:
        numero_conta = \
            int(input('Informe o número da conta que deseja sacar: '))

    conta = recuperar_conta_cliente(cliente, numero_conta)
    valor = float(input('Informe o valor do saque: '))
    cliente.realizar_transacao(conta, transacao=Saque(valor))


def exibir_extrato(clientes: list[object]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        print("\n@@@ Operação falhou! Cliente não encontrado. @@@")
        return

    numero_conta = 0
    if len(cliente.contas) > 1:
        numero_conta = \
            int(input('Informe o número da conta que deseja sacar: '))

    conta = recuperar_conta_cliente(cliente, numero_conta)
    historico: Historico = conta.historico

    print('\n================ EXTRATO ================')
    extrato = ''
    if not historico.transacoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in historico.transacoes:
            extrato += (
                f"\n{transacao['data']}\n{transacao['tipo']}:"
                f"\n\tR$ {transacao['valor']:.2f}"
            )

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('==========================================')
