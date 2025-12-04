# functions.py
"""
Utility Toolkit - Day 4
Safe, minimal, and production-aware implementations of common helpers.
Includes robust input validation, safe CLI parsing, and JSONL history logging.
"""

from typing import Any, Dict, Iterable, List, Union, Optional
import math
import string
import json
import ast
from datetime import datetime
import sys

Number = Union[int, float]


def is_prime(num: int) -> bool:
    """Return True if num is a prime integer. Validate type and handle <2."""
    if not isinstance(num, int):
        raise TypeError("num must be an integer")
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    limit = int(math.isqrt(num))
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """Iterative factorial. Raise for non-int or negative inputs."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> List[int]:
    """Return first n Fibonacci numbers. n must be non-negative int."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def count_vowels(s: str) -> int:
    """Count vowels (a,e,i,o,u) case-insensitive. Validate input string."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return sum(1 for ch in s.lower() if ch in "aeiou")


def reverse_string(s: str) -> str:
    """Return reversed string. Validate input string."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return s[::-1]


def get_unique_elements(lst: Iterable[Any]) -> List[Any]:
    """Return list of unique elements preserving first-seen order."""
    try:
        iterator = iter(lst)
    except TypeError:
        raise TypeError("lst must be iterable")
    seen = set()
    unique = []
    for item in iterator:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a new dict merging dict1 and dict2; dict2 overrides. Validate types."""
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("both arguments must be dicts")
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def find_maximum(lst: Iterable[Number]) -> Number:
    """Return maximum value from iterable. Raise ValueError for empty iterable."""
    try:
        iterator = iter(lst)
    except TypeError:
        raise TypeError("lst must be iterable")
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("lst is empty")
    current_max = first
    for item in iterator:
        if item > current_max:
            current_max = item
    return current_max


def flatten_list(nested_lst: Iterable[Any]) -> List[Any]:
    """Flatten nested lists/tuples into a flat list. Strings are not expanded."""
    try:
        iterator = iter(nested_lst)
    except TypeError:
        raise TypeError("nested_lst must be iterable")

    def _gen(seq):
        for item in seq:
            if isinstance(item, (list, tuple)):
                yield from _gen(item)
            else:
                yield item

    return list(_gen(nested_lst))


def calculate_stats(lst: Iterable[Number]) -> Dict[str, Number]:
    """Return dict with mean, min, max, sum, length. Validate numeric items."""
    try:
        nums = list(lst)
    except TypeError:
        raise TypeError("numbers must be iterable")
    if not nums:
        raise ValueError("numbers is empty")
    for x in nums:
        if not isinstance(x, (int, float)):
            raise TypeError("all items must be int or float")
    total = sum(nums)
    length = len(nums)
    return {
        "mean": total / length,
        "min": min(nums),
        "max": max(nums),
        "sum": total,
        "length": length,
    }


def is_palindrome(s: str) -> bool:
    """Return True if s is palindrome (alphanumeric only), case-insensitive."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor. Validate integer inputs."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return least common multiple. Validate integer inputs."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def apply_discount(price: Number, discount: Number) -> float:
    """Apply percent discount (0-100). Validate numeric inputs."""
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("price and discount must be numbers")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    return float(price * (1 - discount / 100.0))


def clean_text(text: str) -> str:
    """Lowercase and remove punctuation from text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower().strip()


def sentence_to_words(sentence: str) -> List[str]:
    """Split sentence into cleaned words."""
    if not isinstance(sentence, str):
        raise TypeError("sentence must be a string")
    return [w for w in clean_text(sentence).split() if w]


# -----------------------------
# History logging utility
# -----------------------------
def save_history(entry: Dict[str, Any], filename: str = "utility_history.jsonl") -> None:
    """
    Append a single JSON object (entry) as a new line to filename.
    Entry should be a dict describing: function, input, output, timestamp(optional), notes(optional).
    This function injects a UTC timestamp and silently ignores file write errors.
    """
    if not isinstance(entry, dict):
        raise TypeError("entry must be a dict")
    entry.setdefault("ts", datetime.utcnow().isoformat() + "Z")
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        # Non-fatal: do not crash the main program if logging fails
        return


# -----------------------------
# CLI helpers (safe parsing)
# -----------------------------
def _safe_literal_eval(user_input: str):
    """
    Try to parse Python literal (list/dict/number). Fall back to token parsing with numeric casts.
    Returns: parsed python object (int/float/str/list/etc.)
    """
    try:
        return ast.literal_eval(user_input)
    except Exception:
        tokens = user_input.strip().split()
        if not tokens:
            return []
        if len(tokens) == 1:
            tok = tokens[0]
            for cast in (int, float):
                try:
                    return cast(tok)
                except (ValueError, TypeError):
                    continue
            return tok
        out = []
        for t in tokens:
            for cast in (int, float):
                try:
                    out.append(cast(t))
                    break
                except (ValueError, TypeError):
                    continue
            else:
                out.append(t)
        return out


# Minimal CLI example (safe exit and logging)
if __name__ == "__main__":
    print("Utility toolkit loaded.")
    print("Available functions:")
    print("1: check prime number")
    print("2: factorial ")
    print("3: fibonacci sequence")
    print("4: count vowels in string")
    print("5: reverse string")
    print("6: get unique elements from list")
    print("7: merge two dictionaries")
    print("8: find maximum in list")
    print("9: flatten nested list")
    print("10: calculate statistics of numbers")
    print("11: check if string is palindrome")
    print("12: compute GCD of two numbers")
    print("13: compute LCM of two numbers")
    print("14: apply discount to price")
    print("15: clean text (lowercase, remove punctuation)")
    print("16: split sentence into words")



    try:
        n = int(input("enter your utility function number (1-16): ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(1)

    try:
        if n == 1:
            val = int(input("enter number: ").strip())
            out = is_prime(val)
        elif n == 2:
            val = int(input("enter number: ").strip())
            out = factorial(val)
        elif n == 3:
            val = int(input("enter the number : ").strip())
            out = fibonacci(val)
        elif n == 4:
            s = input("enter string: ")
            out = count_vowels(s)
        elif n == 5:
            s = input("enter string: ")
            out = reverse_string(s)
        elif n == 6:
            raw = input("enter list elements (python literal or space-separated): ")
            parsed = _safe_literal_eval(raw)
            out = get_unique_elements(parsed)
        elif n == 7:
            raw1 = input("enter first dict (python literal): ")
            raw2 = input("enter second dict (python literal): ")
            d1 = _safe_literal_eval(raw1)
            d2 = _safe_literal_eval(raw2)
            if not isinstance(d1, dict) or not isinstance(d2, dict):
                raise TypeError("Both inputs must be dicts (e.g. {'a':1}).")
            out = merge_dicts(d1, d2)
        elif n == 8:
            raw = input("enter list elements (python literal or space-separated): ")
            parsed = _safe_literal_eval(raw)
            if not isinstance(parsed, list):
                parsed = [parsed]
            nums = [int(x) for x in parsed]
            out = find_maximum(nums)
        elif n == 9:
            raw = input("enter nested list (python literal): ")
            parsed = _safe_literal_eval(raw)
            out = flatten_list(parsed)
        elif n == 10:
            raw = input("enter list elements (python literal or space-separated): ")
            parsed = _safe_literal_eval(raw)
            if not isinstance(parsed, list):
                parsed = [parsed]
            numbers = [float(x) for x in parsed]
            out = calculate_stats(numbers)
        elif n == 11:
            s = input("enter string: ")
            out = is_palindrome(s)
        elif n == 12:
            a = int(input("enter first number: ").strip())
            b = int(input("enter second number: ").strip())
            out = gcd(a, b)
        elif n == 13:
            a = int(input("enter first number: ").strip())
            b = int(input("enter second number: ").strip())
            out = lcm(a, b)
        elif n == 14:
            price = float(input("enter price: ").strip())
            discount = float(input("enter discount percentage: ").strip())
            out = apply_discount(price, discount)
        elif n == 15:
            text = input("enter text: ")
            out = clean_text(text)
        elif n == 16:
            sentence = input("enter sentence: ")
            out = sentence_to_words(sentence)
        else:
            raise ValueError("Invalid utility function number.")
    except Exception as exc:
        print("Error:", exc)
        # Log the failure and exit gracefully
        try:
            save_history({"function_number": n, "error": str(exc)})
        except Exception:
            pass
        sys.exit(1)

    print("Result:", out)
    # Save a compact history entry with timestamp
    save_history({"function_number": n, "output": out})

