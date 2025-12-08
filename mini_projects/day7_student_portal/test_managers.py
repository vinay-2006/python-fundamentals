# tests/test_managers.py
import unittest
from marks import MarksManager
from fees import FeesManager
from student import Student, StudentValidationError
from datetime import datetime

class TestMarksManager(unittest.TestCase):
    
    def test_initialization(self):
        m = MarksManager({"math": 90, "science": 85})
        self.assertEqual(m.as_dict(), {"math": 90.0, "science": 85.0})
        
    def test_set_mark_valid(self):
        m = MarksManager()
        m.set_mark("physics", 75.5)
        self.assertEqual(m.get_mark("physics"), 75.5)
        m.set_mark("physics", 80) # Update
        self.assertEqual(m.get_mark("physics"), 80.0)

    def test_set_mark_invalid_score(self):
        m = MarksManager()
        # Edge cases: < 0 and > 100
        with self.assertRaisesRegex(ValueError, "Score must be between 0 and 100"):
            m.set_mark("bad_score", 101)
        with self.assertRaisesRegex(ValueError, "Score must be between 0 and 100"):
            m.set_mark("bad_score", -10)
            
    def test_set_mark_empty_subject(self):
        m = MarksManager()
        with self.assertRaisesRegex(ValueError, "Subject name cannot be empty"):
            m.set_mark(" ", 50)
        with self.assertRaisesRegex(ValueError, "Subject name cannot be empty"):
            m.set_mark("", 50)

    def test_remove_mark(self):
        m = MarksManager({"math": 90, "science": 85})
        m.remove_mark("math")
        self.assertIsNone(m.get_mark("math"))
        m.remove_mark("nonexistent") # Should not raise error

    def test_average(self):
        # Test non-empty
        m = MarksManager({"A": 100, "B": 90, "C": 80})
        self.assertAlmostEqual(m.average(), 90.0)
        # Test empty
        m_empty = MarksManager()
        self.assertEqual(m_empty.average(), 0.0)

class TestFeesManager(unittest.TestCase):
    
    def test_initialization(self):
        f = FeesManager(total=1000, paid=200)
        self.assertEqual(f.total, 1000.0)
        self.assertEqual(f.paid, 200.0)
        self.assertEqual(f.balance(), 800.0)
        
    def test_set_total_invalid(self):
        f = FeesManager()
        with self.assertRaises(ValueError):
            f.set_total(-10)

    def test_pay_valid(self):
        f = FeesManager(total=1000, paid=0)
        f.pay(500)
        self.assertEqual(f.paid, 500.0)
        
    def test_pay_overpayment_attempt(self):
        f = FeesManager(total=1000, paid=500)
        # Edge case: overpayment
        with self.assertRaisesRegex(ValueError, "Overpayment is not allowed"):
            f.pay(500.01)

    def test_pay_invalid_amount(self):
        f = FeesManager(total=1000, paid=0)
        with self.assertRaisesRegex(ValueError, "must be positive"):
            f.pay(0)
        with self.assertRaisesRegex(ValueError, "must be positive"):
            f.pay(-100)

    def test_payment_history_record(self):
        f = FeesManager(total=1000, paid=0)
        f.pay(100)
        self.assertEqual(len(f.history), 1)
        self.assertEqual(f.history[0]['amount'], 100.0)
        # Check for timestamp format (ISO 8601)
        self.assertIsInstance(datetime.fromisoformat(f.history[0]['ts']), datetime)
        
    def test_can_pay_helper(self):
        f = FeesManager(total=1000, paid=900)
        self.assertTrue(f.can_pay(100))
        self.assertFalse(f.can_pay(100.01))
        self.assertFalse(f.can_pay(0))
        
class TestStudent(unittest.TestCase):
    
    def test_student_validate_success(self):
        s = Student(1, "Valid Name", "CS", 3)
        # Should not raise an exception
        s.validate()

    def test_student_validate_failure(self):
        # Empty Name
        with self.assertRaisesRegex(StudentValidationError, "name cannot be empty"):
            Student(1, "", "CS", 3).validate()
            
        # Invalid Year Range
        with self.assertRaisesRegex(StudentValidationError, "Year must be between 1 and 5"):
            Student(1, "Name", "CS", 6).validate()
            
        # Empty Branch (due to whitespace removal in init)
        with self.assertRaisesRegex(StudentValidationError, "branch cannot be empty"):
            Student(1, "Name", "  ", 3).validate()

if __name__ == '__main__':
    unittest.main()