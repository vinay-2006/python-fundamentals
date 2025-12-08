# tests/test_persistence.py
import unittest
import os
import shutil
from pathlib import Path
from student import Student, StudentValidationError
from storage import load_students_map, save_students_map

# Setup a temporary directory for testing file I/O
TEST_DIR = Path("temp_test_data")
TEST_FILE = TEST_DIR / "test_students.json"

class TestPersistence(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Create a temporary directory before running tests."""
        if TEST_DIR.exists():
            shutil.rmtree(TEST_DIR)
        TEST_DIR.mkdir()

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary directory after running tests."""
        if TEST_DIR.exists():
            shutil.rmtree(TEST_DIR)

    def setUp(self):
        """Ensure the test file is clean before each test."""
        if TEST_FILE.exists():
            os.remove(TEST_FILE)
            
    def _create_sample_student(self, sid: int) -> Student:
        """Helper to create a fully populated student object."""
        s = Student(sid, f"Test {sid}", "IT", 2)
        s.marks.set_mark("Python", 95)
        s.marks.set_mark("SQL", 80)
        s.fees.set_total(5000)
        s.fees.pay(1000)
        s.fees.pay(500)
        return s

    def test_serialization_round_trip(self):
        """Tests saving and loading data preserves all information accurately."""
        student1 = self._create_sample_student(1)
        student2 = self._create_sample_student(2)
        student_map_original = {1: student1, 2: student2}

        # 1. Save the map
        save_students_map(student_map_original, TEST_FILE)
        self.assertTrue(TEST_FILE.exists())

        # 2. Load the map
        student_map_loaded = load_students_map(TEST_FILE)
        self.assertEqual(len(student_map_original), len(student_map_loaded))

        # 3. Assert deep equality (by comparing to_dict() results)
        self.assertEqual(student_map_original[1].to_dict(), student_map_loaded[1].to_dict())
        self.assertEqual(student_map_original[2].to_dict(), student_map_loaded[2].to_dict())

    def test_load_non_existent_file(self):
        """Tests loading when the data file does not exist."""
        loaded_map = load_students_map(TEST_FILE)
        self.assertEqual(loaded_map, {})
        
    def test_load_corrupt_json(self):
        """Tests loading a file with invalid JSON content."""
        with open(TEST_FILE, 'w') as f:
            f.write("{'1': 'invalid json'}") # Invalid JSON format

        with self.assertRaises(IOError):
            load_students_map(TEST_FILE)

    def test_load_file_with_invalid_student_data(self):
        """Tests loading a file where one record violates Student validation (e.g., empty name)."""
        # Corrupt data (name is empty string)
        corrupt_data = {
            "1": {"id": 1, "name": "Valid", "branch": "CS", "year": 2, "marks": {}, "fees": {}},
            "2": {"id": 2, "name": "", "branch": "CS", "year": 2, "marks": {}, "fees": {}} # This record is invalid
        }
        
        # Save requires to_dict() which calls validate(), so we save the raw dict:
        import json
        with open(TEST_FILE, 'w') as f:
             json.dump(corrupt_data, f)
        
        # The load function should try to load, catch the StudentValidationError for SID 2, log it, 
        # and skip that record, returning only the valid record (SID 1).
        
        loaded_map = load_students_map(TEST_FILE)
        self.assertIn(1, loaded_map)
        self.assertNotIn(2, loaded_map)
        self.assertEqual(len(loaded_map), 1)