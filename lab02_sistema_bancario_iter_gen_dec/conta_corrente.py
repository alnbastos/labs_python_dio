from datetime import datetime


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor) -> bool:
        """Faz um deposito de um valor ao saldo da conta."""
        if valor > 0:
            self._saldo += valor
            print('\n=== Depósito realizado com sucesso! ===')
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
            return False

        return True

    def sacar(self, valor) -> bool:
        """Faz o saque de um valor do saldo da conta."""
        if valor > self._saldo:
            print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')

        elif valor > 0:
            self._saldo -= valor
            print('\n=== Saque realizado com sucesso! ===')
            return True

        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor) -> bool:
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

    def gerar_relatorio(self, tipo_transacao: str = None):
        for transacao in self._transacoes:
            if not tipo_transacao or (
                transacao.get('tipo').lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []

        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao.get('data'), '%d-%m-%Y %H:%M:%S'
            ).date()

            if data_atual == data_transacao:
                transacoes.append(transacao)

        return transacoes
