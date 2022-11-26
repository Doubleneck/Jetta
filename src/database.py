import sqlite3
from db_connection import get_connection

class Database:

    def __init__(self, path = "test.db"):
        self.db_type = "sqlite3_file"  # Not yet maybe later
        self.db_path = path
        self.connection = get_connection()

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.isolation_level = None
        return self.connection

    # Not yet maybe later
    def disconnect(self):
        try:
            self.connection.close()
        except Exception as e:
            raise ConnectionError("Error closing connection to db") from e

    def create_tables(self):
        cursor = self.connection.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS users(\
                           user_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                           username VARCHAR (20) UNIQUE NOT NULL CHECK (username <> ''),\
                           password TEXT NOT NULL CHECK (password <> ''));"
        cursor.execute(create_table)
        self.connection.commit()
        cursor.close()

    def drop_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS users;")
        self.connection.commit()

    def initialize_database(self):
        self.drop_tables()
        self.create_tables()

database = Database()