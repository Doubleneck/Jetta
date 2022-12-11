from flask import render_template, redirect, url_for, request, flash, session
from repositories.note_repository import Note
from services.user_service import the_user_service
from services.note_service import the_note_service
from services.bib_service import the_bib_service
from util import send_string_as_file
from app import app
from database import the_database


def check_signed_in():
    username = session.get("username")
    if not username or username == "":
        flash("Please sign in first.")
        return False
    return True

class CredentialsError(Exception):
    pass


def redirect_to_login():
    return redirect(url_for("login_page"))


def redirect_to_register():
    return redirect(url_for("register_page"))


def redirect_to_main():
    return redirect(url_for("main_page"))


@app.route("/tests/reset", methods=["POST"])
def reset_application():
    the_database.reset_database()
    return "Database Reset"


@app.route("/", methods=["POST", "GET"])
def login_page():
    if request.method != "POST":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    try:
        the_user_service.sign_in(username, password)
        session["username"] = username
        user_id = the_user_service.get_user_id_by_username(username)
        session["user_id"] = user_id
        return redirect_to_main()
    except Exception as error:
        flash(str(error))
        return redirect_to_login()


@app.route("/register", methods=["POST", "GET"])
def register_page():
    if request.method != "POST":
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]

    try:
        the_user_service.create_user(username, password, password_confirm)
        session["username"] = username
        user_id = the_user_service.get_user_id_by_username(username)
        session["user_id"] = user_id
        return redirect_to_main()
    except Exception as error:
        flash(str(error))
        return redirect_to_register()


@app.route("/main", methods=["POST", "GET"])
def main_page():
    if not check_signed_in():
        return redirect("/")

    if request.method == "POST":
        return redirect_to_main()

    user = session["username"]
    user_id = session["user_id"]
    notes = the_note_service.get_all_notes_by_user_id(user_id)

    return render_template("note_listing.html", username=user, user_id=user_id, notes=notes)


@app.route("/create_note")
def create_note_page():
    if not check_signed_in():
        return redirect("/")
    return render_template("create_note.html")


@app.route("/create_new_note", methods=["POST", "GET"])
def create_new_reference():
    if not check_signed_in():
        return redirect("/")

    note = Note(
        author=request.form["author"],
        title=request.form["title"],
        year=request.form["year"],
        doi_address=request.form["doi_address"],
        bib_category=request.form["bib_category"],
        bib_citekey=request.form["bib_citekey"],
    )

    try:
        the_note_service.validate_note(note)
    except ValueError as error:
        flash(str(error))
        return redirect("/create_note")

    user_id = session["user_id"]
    try:
        the_note_service.create_note(user_id, note)
        flash("New reference created successfully!")
    except ValueError as error:
        flash(str(error))
    
    return redirect("/create_note")


@app.route("/download_bibtex", methods=["POST", "GET"])
def download_bibtex():
    if not check_signed_in():
        return redirect("/")

    bib_string = the_note_service.get_notes_as_bib(session["user_id"])
    return send_string_as_file(bib_string, "references.bib")

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


@app.route("/logout", methods=["GET"])
def logout():
    if not check_signed_in():
        return redirect("/")

    del session["username"]
    del session["user_id"]
    return redirect_to_login()
