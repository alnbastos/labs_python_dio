from db.base_repository import BaseRepository


class AlunoRepository(BaseRepository):
    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ra TEXT NOT NULL UNIQUE,
                ano_nascimento INTEGER NOT NULL
            );
        """
        self.execute(query)

    def insert(self, nome: str, ra: str, ano_nascimento: str):
        try:
            query = """
                INSERT INTO alunos (nome, ra, ano_nascimento)
                VALUES (?, ?, ?);
            """
            self.execute(query, (nome, ra, ano_nascimento))
        except Exception as e:
            print("[ROLLBACK] Ocorreu erro ao INSERIR:", e)
            self.connection.rollback()

    def get(self) -> list:
        return self.get_all(name_table="alunos")
