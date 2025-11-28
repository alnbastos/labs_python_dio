from cliente import PessoaFisica, Cliente
from conta_corrente import ContaCorrente


class ContaIterador:
    pass


def log_transacao(funcao):

    def envelope(*args, **kargs):
        print('entrou no log')
        funcao(*args, **kargs)

    return envelope


def filtrar_cliente(cpf: str, clientes: list[PessoaFisica]) -> Cliente | None:
    """Filtra cliente pelo cpf. Evita duplicidade."""
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None


def recuperar_conta_cliente(cliente: PessoaFisica) -> ContaCorrente | None:
    if not cliente.contas:
        print('@@@ Operação falhou! Cliente não possui conta! @@@')
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]
