import sys
from note_manager import NoteManager
from storage import Storage

def print_usage():
    print("Использование: python main.py [команда] [опции]")
    print("Команды:")
    print(" add 'заголовок' 'текст' - Добавить новую заметку")
    print(" update 'id' 'новый заголовок' 'новый текст' - Обновить заметку")
    print(" delete 'id' - Удалить заметку")
    print(" show 'id' - Показать заметку")

if __name__ == "__main__":
    storage = Storage("notes.json", format='json')  # Можно изменить на 'csv'
    manager = NoteManager(storage)

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == 'add' and len(sys.argv) == 4:
        manager.add_note(sys.argv[2], sys.argv[3])
    elif command == 'update' and len(sys.argv) == 5:
        manager.update_note(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == 'delete' and len(sys.argv) == 3:
        manager.delete_note(sys.argv[2])
    elif command == 'show' and len(sys.argv) == 3:
        note = manager.get_note(sys.argv[2])
        if note:
            print(f"ID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.body}\nДата создания: {note.created_at}\nДата обновления: {note.updated_at}")
        else:
            print("Заметка не найдена")
    else:
        print_usage()
