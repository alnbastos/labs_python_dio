from sqlite3 import Row
from db.connection import DatabaseConnection


class BaseRepository:
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = Row

    def execute(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def execute_many(self, query: str, params: list[tuple] = []):
        self.cursor.executemany(query, params)
        self.connection.commit()

    def get_all(self, name_table: str):
        return self.cursor.execute(f"SELECT * FROM {name_table};").fetchall()
