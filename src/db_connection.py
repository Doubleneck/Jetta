import sqlite3

the_connection = sqlite3.connect("test.db", check_same_thread=False)
the_connection.row_factory = sqlite3.Row
