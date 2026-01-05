from db.aluno_repository import AlunoRepository
from db.materia_repository import MateriaRepository
from db.aluno_materia_repository import AlunoMateriaRepository


def display_records(objs: object):
    for obj in objs.get():
        print(dict(obj))


aluno = AlunoRepository()
aluno.create_table()
aluno.insert("João", "123456", "2000")
display_records(aluno)

materia = MateriaRepository()
materia.create_table()
materia.insert_many([
    ("Matemática",),
    ("Português",),
    ("Artes",),
    ("Geografia",),
])
display_records(materia)

aluno_materia = AlunoMateriaRepository()
aluno_materia.criar_tabela()
aluno_materia.link(1, 1)
aluno_materia.link(1, 2)
aluno_materia.link(1, 3)
display_records(aluno_materia)
