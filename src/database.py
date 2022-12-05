import sqlite3
# from db_connection import the_connection


class Database:
    def __init__(self, path="data.db"):
        self.db_path = path
        self.connection = self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        except Exception:
            raise ConnectionError(f"Connection to database ({self.db_path}) failed")
        self.connection.row_factory = sqlite3.Row
        self.connection.isolation_level = None
        self.create_tables()
        return self.connection

    # Not yet maybe later
    def disconnect(self):
        try:
            self.connection.close()
        except Exception as e:
            raise ConnectionError("Error closing connection to db") from e

    def create_tables(self):
        cursor = self.connection.cursor()
        create_table_users = "CREATE TABLE IF NOT EXISTS users(\
                           user_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                           username VARCHAR (35) UNIQUE NOT NULL CHECK (username <> ''),\
                           password TEXT NOT NULL CHECK (password <> ''));"

        create_table_notes = "CREATE TABLE IF NOT EXISTS notes(\
                           notes_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                           user_id INTEGER REFERENCES users NOT NULL,\
                           bib_citekey TEXT,\
                           bib_category TEXT,\
                           author TEXT,\
                           title TEXT,\
                           year TEXT,\
                           doi_address TEXT);"
        cursor.execute(create_table_users)
        cursor.execute(create_table_notes)
        self.connection.commit()
        cursor.close()

    def drop_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("DROP TABLE IF EXISTS notes;")
        self.connection.commit()

    def reset_database(self):
        self.drop_tables()
        self.create_tables()


the_database = Database()
