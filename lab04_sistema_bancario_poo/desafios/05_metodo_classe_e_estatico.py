class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota

    @classmethod
    def criar_aprovado(cls, nome: str):
        return cls(nome, 7)

    @staticmethod
    def nota_valida(nota: float):
        return 0 <= nota <= 10


aluno1 = Aluno('João', 8)
aluno2 = Aluno.criar_aprovado('Maria')

print(Aluno.nota_valida(9))   # True
print(Aluno.nota_valida(15))  # False
