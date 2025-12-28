from utils import filtrar_cliente
from transacao import Transacao


class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: object, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: object):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)


def criar_cliente(clientes: list[PessoaFisica]):
    cpf = input("Informe o CPF (somente número): ")

    if filtrar_cliente(clientes, cpf):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    cliente = PessoaFisica(
        cpf=cpf,
        nome=input("Informe o nome completo: "),
        data_nascimento=input("Informe a data de nascimento (dd-mm-aaaa): "),
        endereco=input("Informe o endereço (logradouro, "
                       "nro - bairro - cidade/sigla estado): "),
    )
    clientes.append(cliente)
    print("=== Usuário criado com sucesso! ===")
