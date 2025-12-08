# student.py
from typing import Optional, Dict
from marks import MarksManager
from fees import FeesManager

class StudentValidationError(Exception):
    """Custom exception for student data validation failures."""
    pass

class Student:
    """Represents a student with personal details, marks, and fees."""
    
    def __init__(self, sid: int, name: str, branch: str, year: int,
                 marks: Optional[Dict[str, float]] = None,
                 fees: Optional[Dict] = None):
        self.id = int(sid)
        self.name = str(name).strip()
        self.branch = str(branch).strip()
        self.year = int(year)
        self.marks = MarksManager(marks or {})
        
        # Initialize FeesManager defensively
        if fees:
            self.fees = FeesManager(total=fees.get("total", 0.0), paid=fees.get("paid", 0.0))
            if "history" in fees:
                # Ensure history is correctly loaded, even if it's an empty list
                self.fees.history = list(fees["history"])
        else:
            self.fees = FeesManager()

    def validate(self):
        """Performs basic validation on student data."""
        if not self.name:
            raise StudentValidationError("Student name cannot be empty.")
        if not self.branch:
            raise StudentValidationError("Student branch cannot be empty.")
        # Sensible year range check
        if self.year < 1 or self.year > 5:
            raise StudentValidationError("Year must be between 1 and 5.")

    def to_dict(self) -> Dict:
        """Converts the Student object and its managers to a dictionary for serialization."""
        self.validate() # Validate before serialization
        return {
            "id": self.id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks.as_dict(),
            "fees": self.fees.as_dict()
        }

    @classmethod
    def from_dict(cls, sid: int, data: dict) -> 'Student':
        """Creates a Student object from a dictionary loaded from storage."""
        instance = cls(sid=int(sid),
                   name=data.get("name", ""),
                   branch=data.get("branch", ""),
                   year=int(data.get("year", 0)),
                   marks=data.get("marks", {}),
                   fees=data.get("fees", {}))
        
        # Validate data upon loading to catch corrupt records
        try:
            instance.validate()
        except StudentValidationError as e:
            # Re-raise with context to indicate data corruption
            raise StudentValidationError(f"Corrupt data for student ID {sid}: {e}")
            
        return instance

    def display_line(self) -> str:
        """Returns a formatted string for viewing the student in the roster."""
        return f"{self.id}\t{self.name}\t{self.branch}\tY{self.year}\tAvg:{self.marks.average():.2f}\tBal:{self.fees.balance():.2f}"