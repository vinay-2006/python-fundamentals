# 🚀 Python Engineering Fundamentals Repository

## Project: Operational Architecture Mode

A dedicated repository for mastering core Python fundamentals through structured practice and the development of integrated, **engineer-grade applications**. The goal is to build a high-quality, reusable toolkit relevant for future work in data science and AIML.

---

## 🧭 Table of Contents

* [📂 Repository Architecture: Detailed Index](#-repository-architecture-detailed-index)
* [✅ Section 1: Completed Mini-Projects (4)](#-section-1-completed-mini-projects-4)
    * [1.1 CLI Calculator](#11-cli-calculator)
    * [1.2 Text Analytics Starter](#12-text-analytics-starter)
    * [1.3 Pattern Generator](#13-pattern-generator)
    * [1.4 Utility Toolkit (v1.0)](#14-utility-toolkit-v10)
* [🏗️ Section 2: Developing Mini-Projects (3)](#️-section-2-developing-mini-projects-3)
* [📚 Section 3: Foundation Core & Practice](#-section-3-foundation-core--practice)
* [▶️ Setup and Execution](#️-setup-and-execution)
* [✨ Engineering Standards & Roadmap](#-engineering-standards--roadmap)

---

## 📂 Repository Architecture: Detailed Index

| Path | Category | Purpose | Content Status |
| :--- | :--- | :--- | :--- |
| **`/practice`** | **Fundamentals** | Holds individual problem sets and solutions for foundational Python features. | Contains **d2\_q1.py**, **d2\_q2.py**, etc. |
| **`/mini_projects`** | **Integrated Projects** | Home for all standalone, fully-functional applications. | **7 Projects** (4 Complete, 3 Developing) |
| **`.github/workflows`** | **Automation** | Placeholder for Continuous Integration (CI) and quality gates. | Ready for integration. |
| **`.gitignore`** | **Configuration** | Excludes cache files, build artifacts, and environment secrets from version control. | Complete. |

---

## ✅ Section 1: Completed Mini-Projects (4)

These four projects are fully developed, committed to `/mini_projects`, and demonstrate mastery of foundational concepts, focusing on robust I/O, user interaction, and modularity.

### 1.1 CLI Calculator
| Feature Focus | Description | Usage Example (Conceptual) |
| :--- | :--- | :--- |
| **CLI Architecture** | Implements argument parsing to handle commands like `add`, `subtract`, etc. | `python calculator.py add 10 5` |
| **Core Logic** | Reliable functions for basic arithmetic operations. | Outputs `15` |
| **Error Handling** | Validates input types and handles division by zero exceptions gracefully. | `python calculator.py divide 10 0` |

### 1.2 Text Analytics Starter
| Feature Focus | Description | Usage Example (Conceptual) |
| :--- | :--- | :--- |
| **Data Structures** | Core use of Lists, Sets, and Dictionaries for efficient data management. | *Processing a paragraph of text.* |
| **NLP Fundamentals** | Performs text cleaning (lowercasing, punctuation removal) and tokenization. | Output includes word frequency table. |
| **File I/O** | Generates a structured analytical summary and saves it to a file (e.g., `report.txt`). | *Generates report.txt* |

### 1.3 Pattern Generator
| Feature Focus | Description | Usage Example (Conceptual) |
| :--- | :--- | :--- |
| **Algorithmic Complexity** | Utilizes nested loops and complex conditional logic to construct various visual patterns. | `python pattern_gen.py pyramid 5` |
| **Pattern Types** | Includes implementations for shapes like Pyramids, Triangles, and Diamonds. | Output: A 5-row star pattern. |
| **User Interaction** | Takes size/height parameters as inputs for dynamic pattern rendering. | |

### 1.4 Utility Toolkit (v1.0)
| Feature Focus | Description | Usage Example (Conceptual) |
| :--- | :--- | :--- |
| **Reusability** | A first-pass at modular design, grouping simple functions (e.g., string formatting, basic math checks) for quick reuse. | *Imported directly by other practice files.* |
| **Functionality** | Includes basic `string_utils` and `math_utils` functions. | `from utility_toolkit import is_prime` |

---

## 🏗️ Section 2: Developing Mini-Projects (3)

These three projects are currently in the development pipeline and represent the next phase of the repository's engineering and diagnostic capabilities.

| Project Name | Scope & Status | Technical Focus |
| :--- | :--- | :--- |
| **5. Python Utility Toolkit (Engineering-Grade Package)** | **Developing** | **Packaging & Distribution:** The next major iteration of the Toolkit. Focus on proper Python package structure, documentation, comprehensive error logging, and preparing for distribution. |
| **6. Log Analyzer (Real-World Diagnostic Tool)** | **Developing** | **File I/O & Diagnostics:** A tool designed to read and parse structured log files (e.g., server logs, custom app logs). Focuses on pattern matching, statistical analysis (frequency of errors/warnings), and reporting. |
| **7. SecureText: Lightweight Encryption/Decryption CLI** | **Developing** | **Security Fundamentals & CLI:** A command-line tool for basic symmetric encryption and decryption. Focuses on safe handling of secrets, robust CLI implementation, and basic cryptographic principles. |

---

## 📚 Section 3: Foundation Core & Practice

The foundation exercises located in the `/practice` folder ensure a solid understanding of Python's most important features before they are integrated into the mini-projects.

| File | Core Concept | Detail |
| :--- | :--- | :--- |
| **`d2_q1.py`** | **Sequences (Lists & Tuples)** | Mastering iterable data structures, including list comprehensions, efficient slicing, and memory management differences between the types. |
| **`d2_q2.py`** | **Mappings & Unordered Collections (Sets & Dictionaries)** | Focused training on the **$O(1)$** lookup efficiency of hashes, advanced dictionary methods, and using sets for unique element identification. |
| *and other practice files...* | *Various* | *Exercises covering conditional logic, loops, function definitions, and basic file operations.* |

---

## ▶️ Setup and Execution

### Prerequisites

All code is written for **Python 3.x**.

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vinay-2006/python-fundamentals.git](https://github.com/vinay-2006/python-fundamentals.git)
    cd python-fundamentals
    ```
2.  **Run any file directly:**
    To execute any completed practice script or project, run it directly with the Python interpreter:
    ```bash
    # Example 1: Running a fundamental exercise
    python practice/d2_q1.py

    # Example 2: Running a mini-project with CLI arguments
    python mini_projects/cli_calculator/calculator.py add 10 2
    ```

---

## ✨ Engineering Standards & Roadmap

This project adheres to a set of high-quality engineering standards:

* **Testing:** All completed projects have **Unit Tests** written (using `pytest` or `unittest`) to ensure reliability and prevent regressions.
* **CI/CD:** The `.github/workflows` folder is designated for a robust **Continuous Integration pipeline** that automatically runs tests and checks code quality on every push.
* **Code Quality:** Strict adherence to **PEP 8** style guide, use of **type hints**, and comprehensive **docstrings** is maintained across the entire codebase.
* **Version Control:** Major releases of the overall toolkit will be tagged using semantic versioning.
