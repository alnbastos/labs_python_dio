def depositar(saldo, valor, extrato, /) -> tuple[float, float]:
    """Faz um deposito de um valor ao saldo da conta (Positional only)."""
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\t+R$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')

    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

    return saldo, extrato


def sacar(
    *, saldo, valor, extrato, limite, numero_saques, limite_saques
) -> tuple[float, float, float]:
    """Faz o saque de um valor do saldo da conta (Keyword only)."""
    if valor > saldo:
        print('@@@ Operação falhou! Você não tem saldo suficiente. @@@')

    elif valor > limite:
        print('@@@ Operação falhou! O valor do saque excede o limite. @@@')

    elif numero_saques >= limite_saques:
        print('@@@ Operação falhou! Número máximo de saques excedido. @@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t-R$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')

    else:
        print('@@@ Operação falhou! O valor informado é inválido. @@@')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato) -> None:
    """(Positional only e Keyword only)."""
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('==========================================')
