# 🛠️ Python Utility Toolkit

A minimal, safe, and robust collection of Python helper functions for mathematics, text processing, data operations, and simple statistics.  
Designed with production awareness, strong input validation, clean return values, and a built-in history logging utility for CLI runs.

---

## ✨ Features

The toolkit includes **16 utility functions**, implemented with strict type and value checks.

### 🔢 Mathematical Utilities
- `is_prime(num)` — Check if an integer is prime.
- `factorial(n)` — Compute factorial (iterative).
- `fibonacci(n)` — Generate the first *n* Fibonacci numbers.
- `gcd(a, b)` — Greatest Common Divisor.
- `lcm(a, b)` — Least Common Multiple.
- `apply_discount(price, discount)` — Apply percentage discount.

### 🔡 String & Text Utilities
- `count_vowels(s)` — Count vowels (case-insensitive).
- `reverse_string(s)` — Reverse a string.
- `is_palindrome(s)` — Check alphanumeric palindrome.
- `clean_text(text)` — Lowercase + remove punctuation.
- `sentence_to_words(sentence)` — Split cleaned text into words.

### 📊 Data & List Utilities
- `get_unique_elements(lst)` — Unique items, order preserved.
- `merge_dicts(dict1, dict2)` — Merge dictionaries (dict2 overrides).
- `find_maximum(lst)` — Manual max() without using max().
- `flatten_list(nested_lst)` — Deep flatten nested lists/tuples.
- `calculate_stats(lst)` — Mean, min, max, sum, length.

---

## 🚀 Usage (Command Line Interface)

The toolkit includes a built-in interactive CLI for quickly testing functions from the terminal.

### Prerequisites
- Python **3.8+** recommended

### Running the Tool

```bash
python utility_toolkit.py
   
PROJECT STRUCTURE :
mini_projects/day4/
├── utility_toolkit.py
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
├── examples/
│   ├── data_processing_demo.py
│   └── read_history.py
└── tests/
    └── test_utility_toolkit.py
```
