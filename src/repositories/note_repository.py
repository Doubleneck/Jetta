from db_connection import the_connection
from flask import session


class NoteRepository:
    def __init__(self, connection=the_connection):
        self.connection = connection

    def create_note(self, bib_citekey, bib_category, author, title, year, doi_address):
        """Create new user bibreference (named as a note) in database. """
        user_id = session["user_id"]
        cursor = self.connection.cursor()
        values = {"user_id": user_id,"bib_citekey": bib_citekey,"bib_category": bib_category,
                  "author": author, "title": title, "year": year, "doi_address": doi_address}
        sql = """INSERT INTO notes (user_id, bib_citekey, bib_category, author, title, year, doi_address)
        VALUES (:user_id, :bib_citekey ,:bib_category, :author, :title, :year, :doi_address)"""
        cursor.execute(sql, values)

        self.connection.commit()
        cursor.close()

    def get_all_notes_by_user_id(self):
        """Returns all notes by user, uses session.user_id as an identifiere"""
        user_id = session["user_id"]
        cursor = self.connection.cursor()
        values = {"user_id": user_id}
        sql = """SELECT * FROM notes
        WHERE user_id=:user_id ORDER BY title"""
        return cursor.execute(sql, values).fetchall()


the_note_repository = NoteRepository()
