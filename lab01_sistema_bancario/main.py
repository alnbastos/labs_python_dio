from cadastros import criar_cliente, criar_conta_corrente
from operacoes_bancarias import depositar, sacar, exibir_extrato

menu = '''

[u] Criar cliente
[c] Criar conta corrente
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
clientes: list[dict] = []
contas_correntes: list[dict] = []


while True:

    opcao = input(menu)

    if opcao == 'u':
        print('\n================ CADASTRO DO CLIENTE ================')

        nome = str(input('Informe o nome: '))
        data_nascimento = str(input('Informe a data de nascimento: '))
        cpf = str(input('Informe o CPF: '))
        endereco = str(input('Informe o endereço: '))

        if any([cliente.get('cpf') == cpf for cliente in clientes]):
            print('Operação falhou! Este CPF já foi cadastrado.')
        else:
            cliente = criar_cliente(nome, data_nascimento, cpf, endereco)
            if cliente:
                clientes.append(cliente)

        print('==========================================')

    elif opcao == 'c':
        print('\n================ CADASTRO DE CONTA CORRENTE ================')

        cpf_cliente = str(input('Informe o CPF do cliente que a conta será vinculada: '))
        cc = criar_conta_corrente(contas_correntes, clientes, cpf_cliente)
        if cc:
            contas_correntes.append(cc)

        print('==========================================')

    elif opcao == 'd':
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
        novo_extrato = exibir_extrato(saldo, extrato=extrato)
        if novo_extrato:
            extrato = novo_extrato

    elif opcao == 'q':
        break

    else:
        print(
            'Operação inválida, '
            'por favor selecione novamente a operação desejada.'
        )
