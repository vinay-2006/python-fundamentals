# marks.py
from typing import Dict, Optional

class MarksManager:
    """Manages subject marks for a student and calculates the average."""
    
    def __init__(self, marks: Optional[Dict[str, float]] = None):
        self._marks = {}
        for k, v in (marks or {}).items():
            self._validate_subject(k)
            self._validate_score(v)
            self._marks[str(k).strip()] = float(v)

    def _validate_score(self, score: float):
        """Validates score is between 0 and 100."""
        if not (0 <= score <= 100):
            raise ValueError(f"Score must be between 0 and 100. Got: {score}.")
            
    def _validate_subject(self, subject: str):
        """Validates subject is a non-empty string."""
        if not subject or not subject.strip():
            raise ValueError("Subject name cannot be empty.")

    def set_mark(self, subject: str, score: float):
        """Sets or updates the score for a subject."""
        self._validate_subject(subject)
        self._validate_score(score)
        self._marks[subject.strip()] = float(score)

    def remove_mark(self, subject: str):
        """Removes a mark for a subject."""
        self._marks.pop(subject.strip(), None)

    def get_mark(self, subject: str) -> Optional[float]:
        """Returns the mark for a subject or None if not found."""
        return self._marks.get(subject.strip())

    def average(self) -> float:
        """Calculates the average score of all subjects."""
        if not self._marks:
            return 0.0
        return sum(self._marks.values()) / len(self._marks)

    def as_dict(self) -> Dict[str, float]:
        """Returns the marks map."""
        return dict(self._marks)