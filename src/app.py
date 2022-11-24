from flask import Flask
import sqlite3
from database import Database

app = Flask(__name__)

@app.route("/")

def index():
    database = Database()
    database.initialize_database()
    database.connection.execute("INSERT INTO users (username, password) VALUES ('kayttaja1', 'test')")
    database.connection.execute("INSERT INTO users (username, password) VALUES ('kayttaja2', 'test')")
    user = database.connection.execute("SELECT username FROM users").fetchall()
    return f"Heipparallaa! {user}"

