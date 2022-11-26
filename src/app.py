from flask import Flask, render_template, redirect, url_for, request, flash, session
from services.user_service import user_service

app = Flask(__name__)
app.secret_key = 'lsefhlashbmihinvittuuntarvitsetsalaista-avaintaflajshgcebOIQROVYW3PVUH'

class CredentialsError(Exception):
    pass



# Urpo_Placeholder_Koodia
class DummyUser:
    def __init__(self, firstname, password):
        self.firstname = firstname
        self.password = password

    def __str__(self):
        return self.firstname

def validate_user(*args):
    for word in args:
        if not word:
            raise CredentialsError("Username or password empty")
    return DummyUser(args[0], args[1]) 



def redirect_to_login():
    return redirect(url_for("login_page"))

def redirect_to_register():
    return redirect(url_for("register_page"))

def redirect_to_main(user):
    return redirect(url_for("main_page", user=user))

@app.route("/", methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            successful_sign_in = user_service.sign_in(username=username, password=password)
            if successful_sign_in:
                session["username"] = username
                return redirect_to_main(user=username)
            else:
                flash("Incorrect username or password")
                return redirect_to_login()
        except CredentialsError as error:
            flash(str(error))
            return redirect_to_login()
    else:
        return render_template('login.html')

@app.route("/register", methods=['POST', 'GET'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if password != password_confirm:
            raise CredentialsError("Password and password confirmation do not match")
        try:
            successful_creation = user_service.create_user(username=username, password=password)
            if successful_creation:
                session["username"] = username
                return redirect_to_main(user=username)
            else:
                return redirect_to_register()
        except CredentialsError as error:
            flash(str(error))
            return redirect_to_register()
    else:
        return render_template('register.html')

@app.route("/main", methods=['POST', 'GET'])
def main_page():
    user = request.args['user']
    if request.method == 'POST':
        return redirect_to_main
    else:
        return render_template('main.html', name=str(user))

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')


