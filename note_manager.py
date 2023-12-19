from note import Note
from storage import Storage

class NoteManager:
    def __init__(self, storage):
        self.storage = storage
        self.notes = self.storage.load_notes()

    def add_note(self, title, body):
        new_id = str(len(self.notes) + 1)
        new_note = Note(new_id, title, body)
        self.notes.append(new_note)
        self.storage.save_notes(self.notes)

    def get_note(self, id):
        for note in self.notes:
            if note.id == id:
                return note

    def update_note(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.update(title, body)
        self.storage.save_notes(self.notes)

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.storage.save_notes(self.notes)
