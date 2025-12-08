# app.py
# Minimal CLI for SMS v1
from storage import load_students, save_students, DEFAULT_FILE
from student import Student
import sys

def next_id(students):
    if not students:
        return 1
    return max(s.id for s in students) + 1

def add_student(students):
    try:
        name = input("Name: ").strip()
        branch = input("Branch: ").strip()
        year = int(input("Year (e.g., 1/2/3/4): ").strip())
    except ValueError:
        print("Invalid input. Aborting add.")
        return
    sid = next_id(students)
    s = Student(sid, name, branch, year, marks=None, fees=None)
    students.append(s)
    print(f"Added student id={s.id}")

def view_students(students):
    if not students:
        print("No students.")
        return
    print("ID\tName\tBranch\tYear\tMarks\tFees")
    for s in students:
        print(s.display_line())

def search_student(students):
    try:
        sid = int(input("Enter student id to search: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    found = next((s for s in students if s.id == sid), None)
    if not found:
        print("Not found.")
        return
    print("Found:")
    print(found.display_line())

def main():
    students = load_students()
    while True:
        print("\nSMS v1 — Select an option")
        print("1 → Add student")
        print("2 → View students")
        print("3 → Search student")
        print("4 → Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            save_students(students)
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
