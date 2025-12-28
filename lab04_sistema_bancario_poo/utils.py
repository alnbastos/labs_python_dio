def filtrar_cliente(clientes: list, cpf: str):
    cliente = [c for c in clientes if c.cpf == cpf]
    return cliente[0] if cliente else None


def recuperar_conta_cliente(cliente: object, numero_conta: int):
    if not cliente.contas:
        print('@@@ Operação falhou! Cliente não possui conta! @@@')
        return

    return cliente.contas[numero_conta-1]
