def depositar(saldo, valor, extrato, /) -> tuple[float, float | None, None]:
    """Faz um deposito de um valor ao saldo da conta (Positional only)."""
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: +R$ {valor:.2f}\n'
        return saldo, extrato

    else:
        print('Operação falhou! O valor informado é inválido.')
        return None, None


def sacar(
    *, saldo, valor, extrato, limite, numero_saques, limite_saques
) -> tuple[float, float, float | None, None, None]:
    """Faz o saque de um valor do saldo da conta (Keyword only)."""
    if valor > saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
        return None, None, None

    elif valor > limite:
        print('Operação falhou! O valor do saque excede o limite.')
        return None, None, None

    elif numero_saques >= limite_saques:
        print('Operação falhou! Número máximo de saques excedido.')
        return None, None, None

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: -R$ {valor:.2f}\n'
        numero_saques += 1
        return saldo, extrato, numero_saques

    else:
        print('Operação falhou! O valor informado é inválido.')
        return None, None, None


def exibir_extrato(saldo, /, *, extrato):
    """(Positional only e Keyword only)."""
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('==========================================')
    return extrato
