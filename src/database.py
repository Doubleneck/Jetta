import sqlite3

class Database:
    def __init__(self, path="data.db"):
        """Construction
        
        Args:
            path: database file
        """

        self.db_path = path
        self.connection = self.connect()

    def connect(self):
        """Try to connect into database, and if fail, raise exception. Also uses create_table method
        
        Returns:
            self.connection: connection to database
        """

        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        except Exception:
            raise ConnectionError(f"Connection to database ({self.db_path}) failed")
        self.connection.row_factory = sqlite3.Row
        self.connection.isolation_level = None
        self.create_tables()
        return self.connection

    def create_tables(self):
        """Creates users and notes tables"""

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
        """Drop users and notes tables if those exists"""

        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("DROP TABLE IF EXISTS notes;")
        self.connection.commit()

    def reset_database(self):
        """Calls drop_tables and create_tables methods"""

        self.drop_tables()
        self.create_tables()


the_database = Database()
