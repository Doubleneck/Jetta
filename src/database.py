import sqlite3

class Database:

    def __init__(self):
        self.db_type = "sqlite3_file" #Not yet maybe later
        self.db_path = "test.db"
        self.connection = self.connect()
    
    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.isolation_level = None
        return connection

    #Not yet maybe later
    def disconnect(self):
        try:
            self.connection.close()
        except Exception as e:
            raise ConnectionError("Error closing connection to db") from e
            
    def create_tables(self):
        create_table ="CREATE TABLE IF NOT EXISTS users(\
                           user_id SERIAL PRIMARY KEY,\
                           username VARCHAR (20) UNIQUE NOT NULL CHECK (username <> ''),\
                           password TEXT NOT NULL CHECK (password <> ''));"
        self.connection.execute(create_table)
        
    def drop_tables(self):
        self.connection.execute("DROP TABLE IF EXISTS users;")
        
    def initialize_database(self):
        self.drop_tables()
        self.create_tables()
