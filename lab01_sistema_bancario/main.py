from operacoes_bancarias import depositar, sacar, visualizar_extrato

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))
        novo_saldo, novo_extrato = depositar(saldo, valor, extrato)
        if novo_saldo and novo_extrato:
            saldo, extrato = novo_saldo, novo_extrato

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        novo_saldo, novo_extrato, novo_n_saques = sacar(
            saldo=saldo, valor=valor, extrato=extrato,
            limite=limite, numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
        if novo_saldo and novo_extrato and novo_n_saques:
            saldo, extrato, numero_saques = (
                novo_saldo, novo_extrato, novo_n_saques
            )

    elif opcao == 'e':
        novo_extrato = visualizar_extrato(saldo, extrato=extrato)
        if novo_extrato:
            extrato = novo_extrato

    elif opcao == 'q':
        break

    else:
        print(
            'Operação inválida, '
            'por favor selecione novamente a operação desejada.'
        )
