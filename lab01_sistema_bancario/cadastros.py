import re


def criar_cliente(nome: str, data_nascimento: str, cpf: str, endereco: str) -> dict:
    def validar_cpf(cpf: str):
        """Validar CPF, apenas números."""
        padrao = r"^\d{11}$"
        return bool(re.match(padrao, cpf))

    if not nome:
        print('Operação falhou! O nome é obrigatório, por favor preencha.')
        return {}

    if not validar_cpf(cpf):
        print('Operação falhou! Preencha o CPF apenas com números.')
        return {}

    return {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
    }


def criar_conta_corrente(contas_correntes: list[dict], clientes: list[dict], cpf_cliente: str):
    agencia = '0001'
    numero_conta = (
        max([cc.get('numero_conta') for cc in contas_correntes]) + 1
        if contas_correntes
        else 1
    )
    cliente = [c.get('nome') for c in clientes if c.get('cpf') == cpf_cliente]

    if not cliente:
        print('Operação falhou! Cliente não encontrado.')
        return {}

    return {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cliente': cliente,
    }
