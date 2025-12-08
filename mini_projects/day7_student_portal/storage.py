# storage.py
import json
import logging
from pathlib import Path
from typing import Dict
from student import Student, StudentValidationError

# Use the logger configured in app.py
logger = logging.getLogger("app")

def load_students_map(filepath: Path | str) -> Dict[int, Student]:
    """Loads student data from a JSON file into a dictionary map."""
    filepath = Path(filepath)
    if not filepath.exists() or filepath.stat().st_size == 0:
        logger.info(f"Data file not found or empty: {filepath}")
        return {}
    try:
        raw = filepath.read_text(encoding="utf-8")
        data = json.loads(raw)
        students = {}
        # data expected as dict of id -> record
        for sid_str, rec in data.items():
            try:
                sid = int(sid_str)
                # Student.from_dict now validates data on load
                students[sid] = Student.from_dict(sid, rec)
            except StudentValidationError as e:
                logger.warning(f"Skipping corrupt student record (ID: {sid_str}): {e}")
                continue
            except Exception as e:
                logger.warning(f"Skipping malformed record (ID: {sid_str}): {e}")
                continue
                
        logger.info(f"Successfully loaded {len(students)} student records.")
        return students
    except Exception as e:
        logger.error(f"Failed to load and parse data from {filepath}: {e}", exc_info=True)
        # Re-raise the exception for top-level handling in app.py
        raise IOError(f"Corrupt or unreadable data file: {filepath}") from e


def save_students_map(students_map: Dict[int, Student], filepath: Path | str) -> None:
    """
    Saves the student map to a JSON file using an atomic write strategy.
    
    The file is first written to a temporary file (.tmp) and then renamed 
    to the final destination. This ensures the data file is never corrupt 
    or incomplete if the save operation is interrupted.
    """
    filepath = Path(filepath)
    obj = {str(sid): student.to_dict() for sid, student in students_map.items()}
    tmp = filepath.with_suffix(".tmp")
    
    try:
        # 1. Write to temporary file
        tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
        
        # 2. Atomically replace the original file
        tmp.replace(filepath)
        logger.info(f"Successfully saved {len(students_map)} student records to {filepath}.")
    except Exception as e:
        logger.error(f"Failed to save data to {filepath}: {e}", exc_info=True)
        # Clean up temporary file if it exists, but the error must be propagated
        if tmp.exists():
            tmp.unlink()
        raise IOError(f"Failed to save data: {filepath}") from e