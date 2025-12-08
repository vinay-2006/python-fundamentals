Includes the quality gate/CI checklist.

```markdown
# 🤝 Contributing to SMS v2

Thank you for considering contributing to the Comprehensive Student Management System! We welcome all contributions, big or small.

## How to Contribute

The standard contribution method is through the "Fork and Pull Request" workflow:

1.  **Fork** the repository on GitHub.
2.  **Clone** your fork locally:
    ```bash
    git clone [https://github.com/your-username/sms-v2.git](https://github.com/your-username/sms-v2.git)
    ```
3.  **Create a new branch** for your feature or fix:
    ```bash
    git checkout -b feat/add-student-search
    ```
4.  **Make your changes.** Please ensure your changes align with the existing Python style and logic.
5.  **Commit** your changes with a clear message (e.g., `fix: Handle invalid fee payment input`).
6.  **Push** your branch to your forked repository.
7.  **Open a Pull Request** (PR) to the original repository's `main` branch.

## Pull Request (PR) Checklist

Before submitting a Pull Request, please ensure the following steps are complete. These are enforced by our CI pipeline:

1.  **Code Style:** Run code formatters (`black`) to ensure code style consistency.
2.  **Linting:** Ensure the code passes all linting checks (`flake8`).
3.  **Tests Pass:** Run `python -m unittest discover tests` and ensure all tests pass.
4.  **Persistence Check:** Confirm the serialization round-trip test passes, guaranteeing data integrity.
5.  **Documentation:** Update the `README.md` or other documentation if any user-facing changes were made.

## Areas for Improvement (Future Features)

* **Search/Filter Functionality:** Implement a function to search for students by name, branch, or ID.
* **Deletion:** Add a function to remove a student record entirely.
* **Marks Summary:** Add a feature to view a ranked list of students based on their average marks.