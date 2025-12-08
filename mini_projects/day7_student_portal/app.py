import sys
import argparse
import logging
import os
from storage import load_students_map, save_students_map
from student import Student, StudentValidationError

# --- Configuration and Setup ---

# Set up basic logging (used by storage.py as well)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
DEFAULT_DATA_FILE = "students.json"

def get_user_input(prompt: str, cast_type=str, min_val: float = None, max_val: float = None):
    """Guards user input with type casting, non-empty, and range checks."""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
            
        if cast_type == str:
            return user_input
            
        try:
            value = cast_type(user_input)
            
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
                
            return value
        except ValueError:
            print(f"Invalid input. Expected a {cast_type.__name__}. Please try again.")


def next_id(students_map: dict) -> int:
    """Returns the next available unique ID."""
    return max(students_map.keys()) + 1 if students_map else 1

def add_student(students_map: dict, data_file: str):
    """Prompts user for student details and adds a new student."""
    print("\n--- Add New Student ---")
    name = get_user_input("Name: ")
    branch = get_user_input("Branch: ")
    # Assuming 4-5 year program
    year = get_user_input("Year: ", cast_type=int, min_val=1, max_val=5) 
    
    sid = next_id(students_map)
    try:
        s = Student(sid, name, branch, year)
        s.validate() # Run defensive validation
        students_map[sid] = s
        save_students_map(students_map, data_file)
        print(f"✅ Added {s.display_line()}")
    except StudentValidationError as e:
        print(f"❌ Cannot add student: {e}")
    except IOError as e:
        print(f"❌ Failed to save student data: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in add_student: {e}", exc_info=True)
        print("❌ An unexpected error occurred while adding student.")


def view_students(students_map: dict):
    """Displays a summary of all students."""
    if not students_map:
        print("No students found.")
        return
    print("\n--- Student Roster ---")
    print("ID\tName\tBranch\tYear\tAvg\tBalance")
    print("-" * 50)
    for s in students_map.values():
        print(s.display_line())
    print("-" * 50)


def manage_fees(students_map: dict, data_file: str):
    """Menu for managing a student's fees."""
    sid = get_user_input("Student ID: ", cast_type=int, min_val=1)
    s = students_map.get(sid)
    if not s:
        print(f"❌ Student with ID {sid} not found.")
        return
    
    while True:
        print(f"\nFees for {s.name} (ID: {sid}): Total {s.fees.total:.2f}, Paid {s.fees.paid:.2f}, Balance {s.fees.balance():.2f}")
        print("Fees Menu: 1 set total, 2 pay, 3 view history, 4 back")
        c = get_user_input("Choice: ", cast_type=str)
        
        if c == "1":
            try:
                total = get_user_input("Total fees: ", cast_type=float, min_val=0.0)
                s.fees.set_total(total)
                save_students_map(students_map, data_file)
                print("✅ Total fees set.")
            except Exception as e:
                print(f"❌ Error setting total fees: {e}")
        elif c == "2":
            try:
                max_pay = s.fees.balance()
                if max_pay <= 0:
                    print("Status: Fees already fully paid or total is zero.")
                    continue
                # Ensure user cannot enter amount greater than balance
                amt = get_user_input(f"Payment amount (Max: {max_pay:.2f}): ", cast_type=float, min_val=0.01, max_val=max_pay)
                s.fees.pay(amt)
                save_students_map(students_map, data_file)
                print("✅ Payment recorded.")
            except Exception as e:
                print(f"❌ Error recording payment: {e}")
        elif c == "3":
            print("\nFee History:")
            if s.fees.history:
                for entry in s.fees.history:
                    print(f"  Amount: {entry['amount']:.2f}, Time: {entry['ts']}")
            else:
                print("  No payment history recorded.")
        elif c == "4":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


def manage_marks(students_map: dict, data_file: str):
    """Menu for managing a student's marks."""
    sid = get_user_input("Student ID: ", cast_type=int, min_val=1)
    s = students_map.get(sid)
    if not s:
        print(f"❌ Student with ID {sid} not found.")
        return

    while True:
        print(f"\nMarks for {s.name} (ID: {sid}): Average {s.marks.average():.2f}")
        print("Marks Menu: 1 set/update, 2 remove, 3 view, 4 back")
        c = get_user_input("Choice: ", cast_type=str)
        
        if c == "1":
            try:
                sub = get_user_input("Subject: ")
                # Validation enforced in MarksManager
                score = get_user_input("Score (0-100): ", cast_type=float, min_val=0.0, max_val=100.0)
                s.marks.set_mark(sub, score)
                save_students_map(students_map, data_file)
                print("✅ Mark set.")
            except Exception as e:
                print(f"❌ Error setting mark: {e}")
        elif c == "2":
            sub = get_user_input("Subject to remove: ")
            if s.marks.get_mark(sub) is not None:
                s.marks.remove_mark(sub)
                save_students_map(students_map, data_file)
                print("✅ Mark removed.")
            else:
                print(f"ℹ️ Subject '{sub}' not found.")
        elif c == "3":
            print("Marks:", s.marks.as_dict())
            print(f"Average: {s.marks.average():.2f}")
        elif c == "4":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


def generate_report(students_map: dict):
    """Generates and displays a detailed report card."""
    sid = get_user_input("Student ID: ", cast_type=int, min_val=1)
    s = students_map.get(sid)
    if not s:
        print(f"❌ Student with ID {sid} not found.")
        return
    
    print("\n--- REPORT CARD ---")
    print(f"ID: {s.id}\nName: {s.name}\nBranch: {s.branch}\nYear: {s.year}")
    print("\nMarks:")
    if s.marks.as_dict():
        for sub, score in s.marks.as_dict().items():
            print(f"  {sub}: {score:.2f}")
    else:
        print("  (No marks recorded)")
        
    print(f"Average: {s.marks.average():.2f}")
    print("\nFees:")
    f = s.fees
    print(f"  Total: {f.total:.2f}  Paid: {f.paid:.2f}  Balance: {f.balance():.2f}")
    
    if f.history:
        print("\n  Recent Payments:")
        for entry in f.history[-3:]: # Show last 3 payments
            # Use os.linesep for cross-platform compatibility, split timestamp for cleaner view
            print(f"    - {entry['amount']:.2f} on {entry['ts'].split('T')[0]}") 
    
    print("-------------------\n")


def parse_args() -> argparse.Namespace:
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Student Management System CLI.")
    parser.add_argument(
        "--data-file", 
        type=str, 
        default=DEFAULT_DATA_FILE,
        help=f"Path to the JSON file for data persistence (default: {DEFAULT_DATA_FILE})."
    )
    return parser.parse_args()


def main():
    """Main application loop."""
    args = parse_args()
    data_file = args.data_file
    
    try:
        students_map = load_students_map(data_file)
        print(f"🚀 Loaded {len(students_map)} students from {data_file}.")
    except Exception as e:
        # Catch explicit IOErrors from storage.py and handle them gracefully
        print(f"🚨 CRITICAL ERROR: Failed to load data from {data_file}. Starting empty.")
        logging.error(f"Load failure: {e}", exc_info=True)
        students_map = {}

    while True:
        print("\nSMS v2 — Main Menu")
        print("1 Add student")
        print("2 View students")
        print("3 Manage Fees")
        print("4 Manage Marks")
        print("5 Generate Report Card")
        print("6 Exit")
        choice = get_user_input("Choice: ", cast_type=str)
        
        if choice == "1":
            add_student(students_map, data_file)
        elif choice == "2":
            view_students(students_map)
        elif choice == "3":
            manage_fees(students_map, data_file)
        elif choice == "4":
            manage_marks(students_map, data_file)
        elif choice == "5":
            generate_report(students_map)
        elif choice == "6":
            try:
                # Save on exit
                save_students_map(students_map, data_file)
                print(f"✅ Saved all data to {data_file}. Exiting.")
            except Exception as e:
                # Catch explicit IOErrors from storage.py
                print(f"🚨 CRITICAL ERROR: Failed to save data on exit: {e}")
                logging.error(f"Save failure on exit: {e}", exc_info=True)
            sys.exit(0)
        else:
            print("Invalid choice. Please select 1 through 6.")

if __name__ == "__main__":
    main()