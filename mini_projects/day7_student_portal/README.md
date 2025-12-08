# 🧑‍🎓 SMS v2: Comprehensive Student Management System (CLI)

This is an enhanced command-line interface (CLI) application developed in Python for managing detailed student records, including academic marks and financial fees.

The project uses object-oriented programming to structure data with persistence handled via JSON file storage, featuring robust input validation and error handling.

## ✨ Features

* **Harden CLI:** Robust input validation and clear error messages.
* **Modular Management:** Dedicated menus for Marks and Fees.
* **Fees Management:** Set total fees, record payments, calculate outstanding balance. Payments are validated against the total to prevent **overpayment**.
* **Marks Management:** Set/update subject scores with **0-100 range validation**.
* **Report Generation:** Comprehensive report card summary.
* **Data Persistence:** Atomic, failure-resistant saving to JSON using the `--data-file` option.

## 🚀 Setup and Run

### Prerequisites

You need **Python 3.8+** installed on your system.

### Running the Application

1.  Clone the repository and navigate into the directory.
2.  Run the main application file from your terminal:

```bash
python app.py
Data Persistence and Configuration
The application uses students.json by default. This file is excluded from Git to prevent accidental committed changes.

To run the application against a clean copy of the seed data or to run multiple independent sessions, use the --data-file option:

Bash

# Use the example seed data for a fresh run
cp students.example.json my_session_data.json
python app.py --data-file my_session_data.json

# You can now track your changes in 'my_session_data.json'
🛠️ Project Structure
app.py: The main entry point, CLI loop, and menu logic.

student.py: Defines the Student class and StudentValidationError.

marks.py: Defines the MarksManager class with input validation.

fees.py: Defines the FeesManager class with payment validation and history.

storage.py: Contains functions to safely load and save data using atomic writes and logging.

students.example.json: Seed data/demo file.

🧪 Testing
The project uses the built-in unittest module. To run all tests from the project root:

Bash

python -m unittest discover tests
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.