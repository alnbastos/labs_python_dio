class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}.')


class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str):
        super().__init__(nome)
        self.matricula = matricula

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e '
              f'minha matrícula é {self.matricula}.')


aluno = Aluno('João', '123456')
aluno.apresentar()
