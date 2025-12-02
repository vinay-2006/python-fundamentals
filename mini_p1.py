# CLI CALCULATOR
"""Simple CLI Calculator with error handling, loop, robust parsing and logging"""
from datetime import datetime

valid_ops = {"+", "-", "*", "**", "/", "//", "%"}

def parse_num(s: str):
    """Parse string to int if possible, otherwise to float.
    Raise ValueError if neither works.
    """
    s = s.strip()
    if not s:
        raise ValueError("Empty number")

    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Can't parse number: {s!r}")

def compute(a, op: str, b):
    """Compute result or raise ValueError for invalid op."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "**":
        return a ** b
    if op == "/":
        return a / b
    if op == "//":
        return a // b
    if op == "%":
        return a % b

    raise ValueError(f"Invalid operation: {op!r}")

def format_result(result):
    """Format float whole numbers as X.0"""
    if isinstance(result, float):
        if result.is_integer():
            return f"{result:.1f}"
        return str(result)
    return str(result)

def log_to_file(a, op, b, display):
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} | {a} {op} {b} = {display}\n")
    except Exception:
        pass  # logging must not break calculator

def repl():
    print("Simple CLI Calculator — supported ops: + - * / // % **")
    print("Enter expressions like: 12 / 3")
    print("Type 'exit' to quit.")

    while True:
        try:
            raw = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            return

        if not raw:
            continue

        if raw.lower() == "exit":
            print("Exiting.")
            return

        # Accept whitespace-separated input
        parts = raw.split()

        # Accept input without spaces: e.g. "12/3"
        if len(parts) == 1:
            for op in sorted(valid_ops, key=len, reverse=True):  # "**" before "*"
                if op in raw:
                    left, right = raw.split(op, 1)
                    parts = [left.strip(), op, right.strip()]
                    break

        if len(parts) != 3:
            print("Format error. Use: <num1> <op> <num2> (e.g. 27 / 3)")
            continue

        a_s, op, b_s = parts

        if op not in valid_ops:
            print(f"Invalid operation. Supported: {' '.join(sorted(valid_ops))}")
            continue

        try:
            a = parse_num(a_s)
            b = parse_num(b_s)
        except ValueError as e:
            print(f"Number parse error: {e}")
            continue

        try:
            result = compute(a, op, b)
        except ZeroDivisionError:
            print("ZeroDivisionError: cannot divide by zero.")
            continue
        except ValueError as e:
            print(e)
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

        display = format_result(result)
        print(f"Result: {display}")
        log_to_file(a, op, b, display)


if __name__ == "__main__":
    repl()
# End of mini_p1.py