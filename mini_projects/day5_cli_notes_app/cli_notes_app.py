import os
from datetime import datetime

NOTES_FILE = "notes.txt"


def ensure_file():
    """Ensure the notes file exists."""
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8"):
            pass


def create_note():
    """Create a new note by appending a timestamped entry."""
    ensure_file()
    content = input("Enter note content: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {content}\n"

    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    print("Note added successfully!")


def read_notes():
    """Return a list of all note lines."""
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]


def update_note():
    """Update a specific note by line number."""
    ensure_file()
    notes = read_notes()

    if not notes:
        print("No notes to update.")
        return

    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note}")

    choice = input("Enter note number to update: ")
    if not choice.isdigit() or int(choice) not in range(1, len(notes) + 1):
        print("Invalid choice.")
        return

    new_content = input("Enter updated content: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[int(choice) - 1] = f"[{timestamp}] {new_content}"

    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

    print("Note updated successfully!")


def delete_note():
    """Delete a specific note by line number."""
    ensure_file()
    notes = read_notes()

    if not notes:
        print("No notes to delete.")
        return

    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note}")

    choice = input("Enter note number to delete: ")
    if not choice.isdigit() or int(choice) not in range(1, len(notes) + 1):
        print("Invalid choice.")
        return

    deleted = notes.pop(int(choice) - 1)

    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

    print(f"Deleted: {deleted}")


def main():
    ensure_file()

    while True:
        print("\n--- Notes CLI App ---")
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                create_note()
            case "2":
                notes = read_notes()
                if not notes:
                    print("No notes available.")
                else:
                    for note in notes:
                        print(note)
            case "3":
                update_note()
            case "4":
                delete_note()
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
