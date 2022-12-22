# from services.note_service import the_note_service

class BibService:

    def generate_bib(self, notes):
        """bibtex parser function

        Args:
            notes (list): A list of note objects to be parsed to bibtex

        Returns:
            String: a string file, which follows bibtex-format
        """
        if len(notes) > 0:
            bibtexString = ""
            for note in notes:
                # the_note_service.validate_note(note)
                bibtexString += "@" + note.bib_category + \
                "{" + note.bib_citekey + "," + "\n\ttitle = {" + note.title + "}," +\
                "\n\tauthor = {" + note.author + "}," + "\n\tyear = {" + note.year + "}," + \
                "\n\tdoi_address = {" + note.doi_address + "}\n}" + "\n"
            return bibtexString

the_bib_service = BibService()
