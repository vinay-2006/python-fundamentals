# CLI Notes App

**Lightweight command-line notes manager with timestamped CRUD support.**

## Features
- Create, Read, Update, Delete (CRUD) notes
- Timestamped entries for traceability
- UTF-8 safe file operations
- Input validation and basic error handling
- Single-file runnable script for easy demonstration

## Requirements
- Python 3.8+

## Usage
1. Clone the repo and change directory:
```bash
git clone <your-repo-url>
cd cli-notes-app
Run the application:

bash
Copy code
python cli_notes_app.py
Use the interactive menu:

1 Create Note

2 Read Notes

3 Update Note

4 Delete Note

5 Exit

Notes file
The application automatically generates notes.txt on first run. Do not create or commit this file manually. notes.txt is included in .gitignore.

Development & Tests
Run tests:

bash
Copy code
python -m unittest discover -s tests
Possible next enhancements
JSON-backed storage with unique IDs

Search / filter by keyword or date range

Export to Markdown or CSV

Unit tests and GitHub Actions CI

Add --file CLI arg to specify storage path

License
MIT