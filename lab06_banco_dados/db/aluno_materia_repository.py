from db.base_repository import BaseRepository


class AlunoMateriaRepository(BaseRepository):

    def criar_tabela(self):
        query = """
            CREATE TABLE IF NOT EXISTS aluno_materia (
                aluno_id INTEGER NOT NULL,
                materia_id INTEGER NOT NULL,
                PRIMARY KEY (aluno_id, materia_id),
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
                    ON DELETE CASCADE,
                FOREIGN KEY (materia_id) REFERENCES materias(id)
                    ON DELETE CASCADE
            );
        """
        self.execute(query)

    def link(self, aluno_id: int, materia_id: int):
        try:
            query = """
                INSERT INTO aluno_materia (aluno_id, materia_id)
                VALUES (?, ?);
            """
            self.execute(query, (aluno_id, materia_id))
        except Exception as e:
            print("[ROLLBACK] Ocorreu erro ao VINCULAR:", e)
            self.connection.rollback()

    def get(self) -> list:
        return self.get_all(name_table="aluno_materia")
