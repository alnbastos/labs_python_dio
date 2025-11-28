import re
import textwrap


def filtrar_cliente(cpf: str, clientes: list[dict]):
    """Filtra cliente pelo cpf. Evita duplicidade."""
    cliente = [cliente for cliente in clientes if cliente.get('cpf') == cpf]
    return cliente[0] if cliente else None


def criar_cliente(clientes: list) -> None:

    def validar_cpf(cpf: str):
        """Validar CPF, apenas números."""
        padrao = r"^\d{11}$"
        return bool(re.match(padrao, cpf))

    cpf = str(input('Informe o CPF (somente números): '))

    if not validar_cpf(cpf):
        print('@@@ Operação falhou! Preencha o CPF apenas com números. @@@')
        return

    if filtrar_cliente(cpf, clientes):
        print('@@@ Operação falhou! Este CPF já foi cadastrado. @@@')
        return

    nome = str(input('Informe o nome: '))
    if not nome:
        print('@@@ Operação falhou!'
              ' O nome é obrigatório, por favor preencha. @@@')
        return

    data_nascimento = str(
        input('Informe a data de nascimento: ')
    )
    endereco = str(
        input('Informe o endereço (logradouro, nro - bairro - cidade/uf): ')
    )

    clientes.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
    })

    print('\n=== Cliente criado com sucesso! ===\n')


def criar_conta_corrente(
    agencia: str, contas_correntes: list[dict], clientes: list[dict]
) -> None:
    cpf_cliente = str(input('Informe o CPF do cliente: '))
    numero_conta = len(contas_correntes) + 1
    cliente = filtrar_cliente(cpf_cliente, clientes)

    if not cliente:
        print('@@@ Operação falhou! Cliente não encontrado. @@@')
        return

    contas_correntes.append({
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cliente': cliente,
    })

    print('\n=== Conta Corrente criado com sucesso! ===\n')


def listar_contas_corrente(contas_corrente: list[dict]):
    for cc in contas_corrente:
        linha = f"""\
            Agência:\t{cc.get('agencia')}
            C/C:\t\t{cc.get('numero_conta')}
            Titular:\t{cc.get('cliente').get('nome')}
        """
        print('='*40)
        print(textwrap.dedent(linha))
