import sqlite3

connection = sqlite3.connect("test.db", check_same_thread=False)

connection.row_factory = sqlite3.Row


def get_connection():
    return connection