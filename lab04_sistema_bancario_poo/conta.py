import textwrap

from cliente import PessoaFisica
from transacao import Historico
from utils import filtrar_cliente


class Conta:
    def __init__(self, numero: int, cliente: PessoaFisica):
        self._saldo = 0
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @classmethod
    def nova_conta(cls, cliente: PessoaFisica, numero: str):
        return cls(cliente=cliente, numero=numero)

    def sacar(self, valor: float) -> bool:
        """Faz o saque de um valor do saldo da conta."""
        if valor > self._saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor: float) -> bool:
        """Faz um deposito de um valor ao saldo da conta."""
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor) -> bool:
        """Valida se o cliente não excedeu o limite, antes de sacar."""
        numeros_saques = len([])

        if valor > self._limite:
            print(
                '\n@@@ Operação falhou! O valor do saque excede o limite. @@@'
            )
        elif numeros_saques >= self._limite_saques:
            print(
                '\n@@@ Operação falhou! Número máximo de saques excedido. @@@'
            )
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\t\tR$ {self.saldo:.2f}
        """


def criar_conta_corrente(
    contas_correntes: list[ContaCorrente], clientes: list[PessoaFisica]
):
    cpf = input("Informe o CPF do cliente: ")
    cliente: PessoaFisica = filtrar_cliente(clientes, cpf)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de "
              "conta encerrado! @@@")
        return

    numero_conta = len(contas_correntes) + 1
    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    contas_correntes.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta Corrente criada com sucesso! ===")


def listar_contas_corrente(contas_correntes: list[ContaCorrente]):
    for conta in contas_correntes:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
