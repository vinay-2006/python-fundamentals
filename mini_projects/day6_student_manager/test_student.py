import unittest
from student import Student

class TestStudent(unittest.TestCase):
    """Unit tests for the Student class in student.py."""

    def test_student_initialization(self):
        s = Student(1, "Test Name", "CS", 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.name, "Test Name")
        self.assertEqual(s.branch, "CS")
        self.assertEqual(s.year, 4)
        self.assertIsNone(s.marks)
        self.assertIsNone(s.fees)

    def test_marks_setter_valid_list(self):
        s = Student(1, "Test", "IT", 3)
        s.marks = [95, 88.5, 70]
        self.assertEqual(s.marks, [95.0, 88.5, 70.0])

    def test_marks_setter_none(self):
        s = Student(1, "Test", "IT", 3, marks=[10])
        s.marks = None
        self.assertIsNone(s.marks)

    def test_marks_setter_invalid_type(self):
        s = Student(1, "Test", "IT", 3)
        with self.assertRaises(ValueError):
            s.marks = "not a list"
        
    def test_fees_setter_valid(self):
        s = Student(1, "Test", "IT", 3)
        s.fees = 5000.75
        self.assertEqual(s.fees, 5000.75)

    def test_fees_setter_zero(self):
        s = Student(1, "Test", "IT", 3)
        s.fees = 0
        self.assertEqual(s.fees, 0.0)

    def test_fees_setter_negative(self):
        s = Student(1, "Test", "IT", 3)
        with self.assertRaises(ValueError):
            s.fees = -10.0

    def test_from_dict_and_to_dict(self):
        original_dict = {
            "id": 5,
            "name": "Alice",
            "branch": "EEE",
            "year": 4,
            "marks": [75, 80.5],
            "fees": 12000.0
        }
        s = Student.from_dict(original_dict)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.name, "Alice")
        self.assertEqual(s.marks, [75.0, 80.5])
        self.assertEqual(s.fees, 12000.0)
        
        # Check if the dict output matches
        self.assertEqual(s.to_dict(), original_dict)

if __name__ == '__main__':
    unittest.main()