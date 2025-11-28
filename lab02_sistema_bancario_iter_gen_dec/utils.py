from cliente import PessoaFisica, Cliente
from conta_corrente import ContaCorrente


class ContaIterador:
    def __init__(self, contas_correntes: list[ContaCorrente]):
        self._contas_correntes = contas_correntes
        self._contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            cc = self._contas_correntes[self._contador]
            self._contador += 1
            return str(cc)
        except IndexError:
            raise StopIteration


def log_transacao(funcao):

    def envelope(*args, **kargs):
        funcao(*args, **kargs)

    return envelope


def filtrar_cliente(cpf: str, clientes: list[PessoaFisica]) -> Cliente | None:
    """Filtra cliente pelo cpf. Evita duplicidade."""
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None


def recuperar_conta_cliente(cliente: PessoaFisica,
                            numero_conta: int = 0) -> ContaCorrente | None:
    if not cliente.contas:
        print('@@@ Operação falhou! Cliente não possui conta! @@@')
        return

    return cliente.contas[numero_conta]
