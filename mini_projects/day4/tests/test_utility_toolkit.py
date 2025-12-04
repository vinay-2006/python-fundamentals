import unittest
import tempfile
import os
import json

from mini_projects.day4.utility_toolkit import (
    is_prime,
    factorial,
    fibonacci,
    count_vowels,
    reverse_string,
    get_unique_elements,
    merge_dicts,
    calculate_stats,
    is_palindrome,
    gcd,
    lcm,
    apply_discount,
    clean_text,
    sentence_to_words,
    _safe_literal_eval,
    save_history,
    flatten_list,
    find_maximum,
)

class TestUtilityToolkit(unittest.TestCase):
    """Test suite for the core functions in utility_toolkit.py."""

    # --- Math / numeric utilities ---
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(18))
        with self.assertRaises(TypeError):
            is_prime(3.5)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(2.5)

    def test_gcd_lcm(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(lcm(15, 20), 60)
        with self.assertRaises(TypeError):
            gcd(3.5, 2)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(100, 10), 90.0)
        with self.assertRaises(ValueError):
            apply_discount(100, 150)
        with self.assertRaises(TypeError):
            apply_discount("100", 10)

    # --- Sequence / list utilities ---
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        with self.assertRaises(TypeError):
            fibonacci(2.5)

    def test_get_unique_elements(self):
        self.assertEqual(get_unique_elements([1, 2, 1, 3]), [1, 2, 3])
        self.assertEqual(get_unique_elements(("a", "b", "a")), ["a", "b"])
        with self.assertRaises(TypeError):
            get_unique_elements(123)

    def test_merge_and_find_max_flatten(self):
        self.assertEqual(merge_dicts({'a': 1}, {'a': 2, 'b': 3})['a'], 2)
        self.assertEqual(find_maximum([1, 5, 3]), 5)
        with self.assertRaises(ValueError):
            find_maximum([])
        self.assertEqual(flatten_list([1, [2, (3, 4)], 5]), [1, 2, 3, 4, 5])

    def test_calculate_stats(self):
        stats = calculate_stats([10, 20, 30])
        expected = {"mean": 20.0, "min": 10, "max": 30, "sum": 60, "length": 3}
        self.assertEqual(stats, expected)
        with self.assertRaises(ValueError):
            calculate_stats([])
        with self.assertRaises(TypeError):
            calculate_stats([1, "a"])

    # --- String utilities ---
    def test_string_utilities(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(clean_text("Hello, WORLD!"), "hello world")
        with self.assertRaises(TypeError):
            count_vowels(123)

    def test_palindrome_and_sentence(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("abc"))
        self.assertEqual(sentence_to_words("  The quick, brown fox "),
                         ["the", "quick", "brown", "fox"])

    # --- Safe literal eval parsing ---
    def test_safe_literal_eval(self):
        self.assertEqual(_safe_literal_eval("[1, 2, 3]"), [1, 2, 3])
        self.assertEqual(_safe_literal_eval("1"), 1)
        self.assertEqual(_safe_literal_eval("1 2 3"), [1, 2, 3])
        self.assertEqual(_safe_literal_eval("hello"), "hello")
        self.assertEqual(_safe_literal_eval(""), [])

    # --- History logging ---
    def test_save_history(self):
        entry = {"function": "is_prime", "input": 7, "output": True}
        with tempfile.TemporaryDirectory() as tmpdir:
            fname = os.path.join(tmpdir, "history_test.jsonl")
            save_history(entry, filename=fname)
            self.assertTrue(os.path.exists(fname))
            with open(fname, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            self.assertEqual(len(lines), 1)
            parsed = json.loads(lines[0])
            self.assertEqual(parsed["function"], "is_prime")
            self.assertEqual(parsed["input"], 7)

if __name__ == "__main__":
    unittest.main()

