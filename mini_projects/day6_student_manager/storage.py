# storage.py -- robust JSON load/save for SMS v1
import json
from typing import List
from pathlib import Path
from student import Student
import shutil

DEFAULT_FILE = Path("students.json")

def _read_text_clean(path: Path) -> str:
    # Read file and remove common BOM and stray control characters at start
    raw = path.read_text(encoding="utf-8", errors="replace")
    # strip BOM if present
    if raw.startswith("\ufeff"):
        raw = raw.lstrip("\ufeff")
    return raw

def load_students(filepath: Path | str = DEFAULT_FILE) -> List[Student]:
    filepath = Path(filepath)
    if not filepath.exists():
        return []

    # If file is empty, treat as empty list
    if filepath.stat().st_size == 0:
        return []

    try:
        text = _read_text_clean(filepath)
        # If the cleaned text is empty/whitespace, return empty
        if not text or text.strip() == "":
            return []
        data = json.loads(text)
        students: List[Student] = []
        for d in data:
            try:
                students.append(Student.from_dict(d))
            except Exception:
                # skip malformed record
                continue
        return students
    except json.JSONDecodeError as e:
        # Backup corrupt file then try a simple repair (if possible)
        backup = filepath.with_suffix(".json.corrupt.bak")
        shutil.copy2(filepath, backup)
        try:
            # attempt quick repair: extract first '[' and last ']' substring
            text = _read_text_clean(filepath)
            start = text.find('[')
            end = text.rfind(']')
            if start != -1 and end != -1 and end > start:
                candidate = text[start:end+1]
                data = json.loads(candidate)
                students = []
                for d in data:
                    try:
                        students.append(Student.from_dict(d))
                    except Exception:
                        continue
                return students
        except Exception:
            pass
        # If repair fails, return empty list (file backed up)
        return []
    except Exception:
        # Any other I/O or unexpected error -> return empty
        return []

def save_students(students: List[Student], filepath: Path | str = DEFAULT_FILE) -> None:
    filepath = Path(filepath)
    tmp = filepath.with_suffix(".tmp")
    data = [s.to_dict() for s in students]
    # Write atomically: write temp file then replace original
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    tmp.replace(filepath)
