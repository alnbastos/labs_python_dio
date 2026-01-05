import sqlite3
from pathlib import Path


class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            root_path = Path(__file__).parent.parent
            cls._connection = sqlite3.connect(root_path / "escola.db")
            cls._connection.execute("PRAGMA foreign_keys = ON;")
        return cls._connection
