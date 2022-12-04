from repositories.note_repository import the_note_repository

class NoteService:
    def __init__(self, repository=the_note_repository):
        self._repository = repository

    def create_note(self, user_id, note):
        self._repository.create_note(user_id, note)
        return True

    def get_all_notes_by_user_id(self, user_id):
        return self._repository.get_all_notes_by_user_id(user_id)

the_note_service = NoteService()
