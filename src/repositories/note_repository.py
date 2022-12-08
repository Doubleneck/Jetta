from flask import session
from database import the_database

class NoteRepository:
    def __init__(self, connection=the_database.connection):
        self.connection = connection

    def create_note(self, user_id, note):
        """Create new user bibreference (named as a note) in database for user_id. """
        cursor = self.connection.cursor()
        values = {"user_id": user_id, "bib_citekey": note.bib_citekey, 
                "bib_category": note.bib_category, "author": note.author, 
                "title": note.title, "year": note.year, "doi_address": note.doi_address}
        sql = """INSERT INTO notes (user_id, bib_citekey, bib_category, author, title, year, doi_address)
        VALUES (:user_id, :bib_citekey, :bib_category, :author, :title, :year, :doi_address)"""
        cursor.execute(sql, values)

        self.connection.commit()
        cursor.close()

    def get_all_notes_by_user_id(self, user_id):
        """Returns all notes for the user with the given user_id"""
        cursor = self.connection.cursor()
        values = {"user_id": user_id}
        sql = """SELECT * FROM notes
        WHERE user_id=:user_id ORDER BY title"""

        # Convert to Note objects instead of depending on the database representation
        # for a more reliable interface
        return [_database_row_to_note(row) for row in cursor.execute(sql, values).fetchall()]
    
    def check_if_citekey_exists(self, citekey):
        """Checks if citekey that is given as parameters already exists

        Args:
            citekey (string): citekey for the bibtex entry
        """
        cursor  = self.connection.cursor()
        values = {"citekey":citekey}
        sql = """SELECT user_id, bib_citekey, bib_category, 
        author, title, year, doi_address
        FROM notes
        WHERE bib_citekey=:citekey"""
        result = cursor.execute(sql, values).fetchall()
        if result:
            return True
        return False


def _database_row_to_note(row):
    return Note(
        bib_citekey = row["bib_citekey"],
        bib_category = row["bib_category"],
        author = row["author"],
        title = row["title"],
        year = row["year"],
        doi_address = row["doi_address"]
    )

class Note:
    def __init__(self, bib_citekey, bib_category, author, title, year, doi_address):
        self.bib_citekey = bib_citekey
        self.bib_category = bib_category
        self.author = author
        self.title = title
        self.year = year
        self.doi_address = doi_address

    def __eq__(self, other):
        if not isinstance(other, Note):
            return False
        return self.bib_citekey == other.bib_citekey\
                and self.bib_category == other.bib_category\
                and self.author == other.author\
                and self.title == other.title\
                and self.year == other.year\
                and self.doi_address == other.doi_address

    def __ne__(self, other):
        return not self == other


the_note_repository = NoteRepository()
