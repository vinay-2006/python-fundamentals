# 📚 SMS v1: Simple Student Management System

A minimal, command-line interface (CLI) application for managing student records.

This project is a simple demonstration of Python class structures, data persistence using JSON, and basic CRUD (Create, Read, Update, Delete - *currently only Create/Read/Search*) operations in a CLI environment.

## ✨ Features

* **Add Student:** Easily enroll a new student with an auto-incremented ID.
* **View Students:** List all current students with a summary of their data.
* **Search Student:** Find a student record by their unique ID.
* **Data Persistence:** Student data is automatically saved to and loaded from `students.json`.

## 🚀 Setup and Run

### Prerequisites

You need **Python 3.6+** installed on your system.

### Installation

No specific installation steps are required beyond having the Python files.

### Running the Application

1.  Make sure all project files (`app.py`, `student.py`, `storage.py`, and `students.json` if it exists) are in the same directory.
2.  Run the main application file from your terminal:

```bash
python app.py