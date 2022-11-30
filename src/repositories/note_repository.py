from db_connection import the_connection
from flask import session


class NoteRepository:

    def create_note(self, bibcategory, author, title, year, doiaddress):
        """Create new user bibreference (named as a note) in database. """
        user_id = session["user_id"]
        cursor = self.connection.cursor()
        values = {"user_id": user_id, "bibcategory": bibcategory,
                  "author": author, "title": title, "year": year, "doiaddress": doiaddress}
        sql = """INSERT INTO notes (user_id, bibcategory, author, title, year, doiaddress)
        VALUES (:user_id, :bibcategory, :author, :title, :year, :doiaddress)"""
        cursor.execute(sql, values)

        self.connection.commit()
        cursor.close()


the_note_repository = NoteRepository()
