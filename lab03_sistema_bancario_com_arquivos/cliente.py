from conta_corrente import Conta


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao):
        if conta and len(conta.historico.transacoes_do_dia()) >= 10:
            print(
                '\n@@@ Operação falhou! Você excedeu o número de transações '
                'permitidas para hoje! @@@'
            )
            return 'FALHA: Limite de transações excedidas.'

        transacao.registrar(conta)

    def adicionar_contas(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self):
        return f'<{self.__class__.__name__}: ("{self.cpf}")>'
