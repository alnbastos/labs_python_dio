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
