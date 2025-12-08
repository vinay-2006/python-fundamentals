# student.py
from typing import Optional

class Student:
    """
    Minimal, production-minded Student model for SMS v1
    Fields:
      - id (int)
      - name (str)
      - branch (str)
      - year (int)
      - marks (Optional[list[float]] or None)
      - fees (Optional[float] or None)
    """

    def __init__(self, sid: int, name: str, branch: str, year: int,
                 marks: Optional[list[float]] = None, fees: Optional[float] = None):
        self.id = int(sid)
        self.name = str(name)
        self.branch = str(branch)
        self.year = int(year)
        # Use "protected" storage pattern for marks/fees
        self._marks = None
        self._fees = None
        self.marks = marks  # uses setter
        self.fees = fees    # uses setter

    # marks property: store list[float] or None
    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value is None:
            self._marks = None
            return
        if not isinstance(value, list):
            raise ValueError("marks must be a list of numbers or None")
        self._marks = [float(x) for x in value]

    # fees property: store non-negative float or None
    @property
    def fees(self):
        return self._fees

    @fees.setter
    def fees(self, value):
        if value is None:
            self._fees = None
            return
        v = float(value)
        if v < 0:
            raise ValueError("fees cannot be negative")
        self._fees = v

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self._marks,
            "fees": self._fees
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Student":
        return cls(
            sid=int(d["id"]),
            name=d["name"],
            branch=d["branch"],
            year=int(d["year"]),
            marks=d.get("marks"),
            fees=d.get("fees")
        )

    def display_line(self) -> str:
        marks_summary = "None" if not self.marks else f"{len(self.marks)} marks"
        fees_summary = "None" if self.fees is None else f"{self.fees}"
        return f"{self.id}\t{self.name}\t{self.branch}\tY{self.year}\t{marks_summary}\tFees:{fees_summary}"
