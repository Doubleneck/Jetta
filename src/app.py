from flask import Flask, render_template
from services.user_service import UserService
import sqlite3
from database import Database

app = Flask(__name__)

@app.route("/")
def index():
    database = Database()
    database.initialize_database()
    user_service = UserService(database)
    database.connection.execute("INSERT INTO users (username, password) VALUES ('kayttaja1', 'test')")
    database.connection.execute("INSERT INTO users (username, password) VALUES ('kayttaja2', 'test')")
    user_service.create_user("eero", "salasana")
    user = database.connection.execute("SELECT username FROM users").fetchall()
    return render_template('login.html')

if __name__=="__main__":
    app.run(host='0.0.0.0')
