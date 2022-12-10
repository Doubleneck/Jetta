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
                self.validate_note(note)
                bibtexString += "@" + note.bib_category + \
                "{" + note.bib_citekey + "," + "\n\ttitle = {" + note.title + "}," +\
                "\n\tauthor = {" + note.author + "}," + "\n\tyear = {" + note.year + "}," + \
                "\n\tdoi_address = {" + note.doi_address + "}\n}" + "\n"
            return bibtexString

    def validate_note(self,note):
        valid_categories = ['book','article','phdthesis','misc']
        if not note.bib_category in valid_categories or \
            note.bib_citekey == '':
            raise ValueError("Bib category must be one of: book, article, phdthesis or misc")
        
        return True

the_bib_service = BibService()
