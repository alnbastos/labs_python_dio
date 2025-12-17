import re
import textwrap

from conta_corrente import ContaCorrente
from cliente import PessoaFisica
from utils import ContaIterador, log_transacao, filtrar_cliente


@log_transacao
def criar_cliente(clientes: list) -> None:
    def validar_cpf(cpf: str):
        """Validar CPF, apenas números."""
        padrao = r"^\d{11}$"
        return bool(re.match(padrao, cpf))

    cpf = input('Informe o CPF (somente números): ')

    if not validar_cpf(cpf):
        print('@@@ Operação falhou! Preencha o CPF apenas com números. @@@')
        return 'FALHA: CPF incorreto.'

    if filtrar_cliente(cpf, clientes):
        print('@@@ Operação falhou! Este CPF já foi cadastrado. @@@')
        return 'FALHA: CPF já cadastrado.'

    cliente = PessoaFisica(
        cpf=cpf,
        nome=input('Informe o nome completo: '),
        data_nascimento=input('Informe a data de nascimento (dd-mm-aaaa): '),
        endereco=input(
            'Informe o endereço (logradouro, nro - bairro - cidade/uf): '
        )
    )

    clientes.append(cliente)

    print('\n=== Cliente criado com sucesso! ===\n')
    return 'SUCESSO'


@log_transacao
def criar_conta_corrente(
    numero_conta: str, contas_correntes: list[ContaCorrente],
    clientes: list[PessoaFisica],
) -> None:
    cpf = str(input('Informe o CPF do cliente: '))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('@@@ Operação falhou! Cliente não encontrado, '
              'fluxo de criação de conta encerrado! @@@')
        return 'FALHA: Cliente não encontrado.'

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas_correntes.append(conta)
    cliente.contas.append(conta)

    print('\n=== Conta Corrente criada com sucesso! ===\n')
    return 'SUCESSO'


def listar_contas_corrente(contas_corrente: list[ContaCorrente]):
    for cc in ContaIterador(contas_corrente):
        print('='*40)
        print(textwrap.dedent(cc))
