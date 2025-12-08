# 🚀 Core Python Engineering Fundamentals — WEEK 1 COMPLETE (7/7 Projects Delivered)

## Focused Mastery: Data Structures, File I/O, and Object-Orienthed Programming (OOP)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Code Status](https://img.shields.io/badge/Codebase-Stable-brightgreen)
![Tests](https://img.shields.io/badge/Unit_Tests-Implemented-success)
![Standards](https://img.shields.io/badge/Standards-PEP8%20%26%20Modular-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

This repository documents the successful completion of an intensive, 7-day program designed to convert foundational Python knowledge into deployable, **test-driven, modular software systems**. Every module reflects real-world engineering standards used in backend development and data workflows.

---

## 📊 Execution Summary

| Metric | Status | Notes |
| :--- | :--- | :--- |
| **Duration** | 7 Days | Structured engineering sprint from 29 Nov – 5 Dec. |
| **Mini-Projects Delivered** | **7 Completed** | End-to-end, functional, and modular applications. |
| **Engineering Focus** | OOP, Persistence, DSA, CLI Architecture | Built production habits early. |
| **Quality Standards** | PEP8 + Type Hints + Docstrings + Unit Tests | Consistency across all modules. |

---

## 🏗️ Technical Value Proposition: Why This Matters

This codebase is a direct demonstration of core engineering capability, moving beyond academic exercises to implement industrial concepts:

* **Modular Design:** Ability to design and implement **testable Python systems** using strong function and class separation.
* **OOP Mastery:** Practical implementation of **inheritance** and **polymorphism** in a real-world data model (Student Management System).
* **Fault-Tolerant Persistence:** Development of **file-based storage layers** (TXT, CSV/JSON) for atomic read/write operations.
* **CLI Architecture:** Development of robust Command-Line Interface (CLI) applications using native Python I/O.
* **Unit-Test-Driven Habit:** Usage of **unit tests** to validate complex business logic and data persistence correctness.

---

## 🔥 Mini-Project Gallery (7 Completed Applications)

The projects below serve as functional demonstrations of the acquired skills. Click the links to navigate directly to the source code.

| Project | Core Skill Focus | Engineering Value | Link to Source |
| :--- | :--- | :--- | :--- |
| **CLI Calculator** | I/O, Error Handling, Functions | Fault-tolerant basic utility. | [Open Source](mini_projects/day1_cli_calculator) |
| **Word Frequency Counter** | DSA (Dicts/Sets/Lists) | Text analysis pipeline starter. | [Open Source](mini_projects/day2_word_counter) |
| **Pattern Generator** | Advanced Flow Control | Algorithmic logic and control. | [Open Source](mini_projects/day3_pattern_generator) |
| **Utility Toolkit (`utils.py`)** | Modularity, Reusability | Building a core internal library. | [Open Source](mini_projects/day4_utility_toolkit) |
| **Notes App (CRUD)** | File Persistence (TXT), State | Simple database emulation. | [Open Source](mini_projects/day5_cli_notes_app) |
| **Student Management (Part 1)** | OOP, CSV/JSON Persistence | Data modeling and storage layer. | [Open Source](mini_projects/day6_student_portal_p1) |
| **Advanced SMS (Part 2)** | Inheritance, Advanced OOP Logic | Complex business rule implementation. | [Open Source](mini_projects/day7_student_portal) |

---

## 💻 SECTION 5: Installation & Execution

### 5.1 Prerequisites

All code is written for **Python 3.x**. Using a virtual environment is strongly recommended for dependency isolation.

### 5.2 Environment Setup

```bash
# 1. Create a virtual environment
python3 -m venv venv

# 2. Activate the environment (macOS/Linux)
source venv/bin/activate

# 3. Activate the environment (Windows)
.\venv\Scripts\activate
5.3 Local Execution
Clone the repository and run any mini-project directly from the terminal.
---
Bash

# 1. Clone the repository
git clone [https://github.com/vinay-2006/python-fundamentals.git](https://github.com/vinay-2006/python-fundamentals.git)
cd python-fundamentals

# 2. Example: Run the Advanced Student Management System
python mini_projects/day7_student_portal/main.py

---
## ⚙️ SECTION 6: Project Showcase - Student Management System (Day 7)
The culminating project demonstrates a complex, multi-state system built on modern OOP principles.

Architecture Diagram: Composition vs. Inheritance
The system is designed with a clear separation of concerns, showing how domain logic is managed by specialized classes.

Code snippet

graph TD
    A[main.py: CLI Entry Point] --> B(SMS Manager Class);
    B --> C(Student Class);
    B --> D(Persistence Layer);
    C --> E(Fees Manager: Business Logic);
    C --> F(Marks Manager: Business Logic);
    D --> G(Data Storage: students.json);
Live Demonstration (CLI Output)
The screenshot below shows the live functionality of the system, including adding a new student and viewing the updated record.

📚 SECTION 7: Repository Architecture
The project structure enforces clean separation between daily training exercises and final modular applications.
Path,Category,Purpose,Content Status
/mini_projects,Integrated Applications,"Home for all 7 end-to-end applications, each with its own folder.",7 Projects Completed.
/practice,Daily Training,"Individual solutions and scripts for fundamental exercises (DSA, Patterns, HackerRank).",Complete.
.github/workflows,CI/CD,Designated folder for Continuous Integration pipelines and automated quality checks.,Ready for integration.
.gitignore,Configuration,"Ensures clean version control by excluding binaries, cache files, and environment secrets.",Complete.
