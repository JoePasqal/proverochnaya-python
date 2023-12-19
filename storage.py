import json
import csv
import os
from note import Note

class Storage:
    def __init__(self, filename, format='json'):
        self.filename = filename
        self.format = format

    def save_notes(self, notes):
        if self.format == 'json':
            with open(self.filename, 'w') as f:
                json.dump([note.__dict__ for note in notes], f)
        elif self.format == 'csv':
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                for note in notes:
                    writer.writerow([note.id, note.title, note.body, note.created_at, note.updated_at])

    def load_notes(self):
        if not os.path.exists(self.filename):
            return []  # Возвращаем пустой список, если файл не существует

        try:
            if self.format == 'json':
                with open(self.filename, 'r') as f:
                    notes_data = json.load(f)
                    return [Note(**data) for data in notes_data]
            elif self.format == 'csv':
                with open(self.filename, 'r') as f:
                    reader = csv.reader(f, delimiter=';')
                    return [Note(row[0], row[1], row[2], row[3], row[4]) for row in reader]
        except json.JSONDecodeError:
            return []  # Возвращаем пустой список, если файл JSON пуст или некорректен

        return []  # Возвращаем пустой список, если не удалось загрузить данные
