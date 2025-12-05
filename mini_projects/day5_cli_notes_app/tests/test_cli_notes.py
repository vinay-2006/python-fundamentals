import os
import unittest
from unittest.mock import patch
from datetime import datetime

import cli_notes_app as app

TEST_FILE = "test_notes.txt"


class TestCliNotesApp(unittest.TestCase):
    def setUp(self):
        app.NOTES_FILE = TEST_FILE
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        app.ensure_file()

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_ensure_file_creates_file(self):
        self.assertTrue(os.path.exists(TEST_FILE))

    @patch("builtins.input", side_effect=["Test note content"])
    def test_create_note_appends_entry(self, _mock_input):
        app.create_note()
        with open(TEST_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Test note content", content)
        self.assertTrue(content.startswith("["))

    def test_read_notes_empty_returns_empty_list(self):
        with open(TEST_FILE, "w", encoding="utf-8"):
            pass
        result = app.read_notes()
        self.assertEqual(result, [])

    def test_read_notes_returns_lines(self):
        lines = [
            "[2024-01-01 10:00:00] Note A\n",
            "[2024-01-02 11:00:00] Note B\n",
        ]
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)
        result = app.read_notes()
        self.assertEqual(len(result), 2)

    @patch("builtins.input", side_effect=["1", "Updated Content"])
    def test_update_note_success(self, _mock_input):
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.write("[2024-01-01 10:00:00] Old Note\n")

        app.update_note()

        with open(TEST_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Updated Content", content)

    @patch("builtins.input", side_effect=["1"])
    def test_delete_note_success(self, _mock_input):
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.write("[2024-01-01 10:00:00] To Delete\n")

        app.delete_note()

        with open(TEST_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("To Delete", content)


if __name__ == "__main__":
    unittest.main()
