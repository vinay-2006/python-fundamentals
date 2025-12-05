Changelog

All notable changes to the cli_notes_app project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

[0.1.0] - 2023-12-06 (Initial Submission)

Added

Core Python application (notes.py) providing Create, Read, Update, and Delete functionality for notes (CRUD).

Data persistence mechanism using local .txt file (notes.txt).

Automated timestamping for new and updated notes.

Initial project structure including README.md, LICENSE, and .gitignore.

Testing framework with tests/test_notes.py using unittest to validate CRUD logic.

CONTRIBUTING.md guide for new collaborators.

pyproject.toml for code style and tool configuration.

Changed

Refactored file handling operations to consistently use the with open(...) context manager.

Project Name updated from Filer-CLI-Notes to cli_notes_app.

Removed

Placeholder code for database connections.

Fixed

Handled FileNotFoundError during reading notes to ensure the app starts cleanly even if notes.txt does not exist.