class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
        else:
            print('Valor de deposito inválido.')

    def sacar(self, valor: float):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
        else:
            print('Saldo insuficiente ou valor inválido.')


conta = ContaBancaria()
conta.depositar(100)
conta.sacar(10)
print(conta.saldo)
