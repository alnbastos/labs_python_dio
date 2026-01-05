from db.base_repository import BaseRepository


class MateriaRepository(BaseRepository):
    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS materias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            );
        """
        self.execute(query)

    def insert(self, nome: str):
        try:
            query = "INSERT INTO materias (nome) VALUES (?);"
            self.execute(query, (nome, ))
        except Exception as e:
            print("[ROLLBACK] Ocorreu erro ao INSERIR:", e)
            self.connection.rollback()

    def insert_many(self, nomes: list[tuple[str]]):
        try:
            query = "INSERT INTO materias (nome) VALUES (?);"
            self.execute_many(query, nomes)
        except Exception as e:
            print("[ROLLBACK] Ocorreu erro ao INSERIR:", e)
            self.connection.rollback()

    def get(self) -> list:
        return self.get_all(name_table="materias")
