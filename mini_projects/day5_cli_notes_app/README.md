# 📝 CLI Notes App

Lightweight command-line notes manager with timestamped CRUD support.

---

## ✨ Features
* ➕ Create, Read, Update, Delete notes (CRUD)
* ⏰ Automatic timestamps
* 🔒 Safe UTF-8 file handling
* ✅ Input validation
* 🧪 Testable logic

---

## 🛠️ Requirements
Python 3.8+

---

## 🚀 Usage

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd cli-notes-app
2. Run the application
```
```Bash

python cli_notes_app.py
3. Menu options
1 → Create Note
2 → Read Notes
3 → Update Note
4 → Delete Note
5 → Exit
```
Notes File
notes.txt is generated automatically. It is ignored through .gitignore and must NOT be committed.

🔬 Running Tests
```Bash

python -m unittest discover -s tests
```
💡 Enhancements (Optional)
💾 JSON-based note storage

🔍 Search and filter

📤 Markdown/CSV export

🤖 GitHub Actions CI

⚙️ CLI argument for custom notes file

📄 License
MIT License
