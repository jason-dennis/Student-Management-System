# Student Management System

A console-based application (CLI) for managing students, subjects, and grades.

I created this project for the **Fundamentals of Programming** course to practice software architecture patterns in Python, specifically focusing on separating the user interface from the business logic.

## Functionality

The application allows the user to:
* **Manage Students:** Add, update, or delete student records.
* **Manage Subjects:** Add or remove subjects from the curriculum.
* **Assign Grades:** Add grades to students for specific subjects.
* **Generate Reports:**
    * Search for students by ID or Name.
    * View students ordered by name or grades.
    * View statistics (e.g., Top 20 students, students with grades above 5).

## Technical Implementation

The project follows a **Layered Architecture** to organize the code:

* **Domain:** Classes defining the data entities (`Student`, `Subject`, `Grade`).
* **Repository (`Structure/`):** Handles data storage. The project implements reading/writing to text files (`.txt`) for persistence.
* **Service (`Business/`):** Contains the logic for processing data and connecting the UI to the Repository.
* **UI:** Handles user input and printing to the console.
* **Validators:** Custom logic to ensure data is correct (e.g., ensuring names are not empty, grades are between 1-10).

### Key Concepts Used

* **Custom Sorting:** Instead of using Python's built-in `.sort()`, I implemented generic sorting algorithms in `Sorting.py` to handle custom criteria (lambdas).
* **Dependency Injection:** Services receive their repositories as parameters, decoupling the logic from the storage method.
* **Unit Testing:** Tests are included in the `Tests/` folder to verify the logic.

## Project Structure

```text
/
├── Business/      # Logic controllers (Services)
├── Domain/        # Entity definitions
├── Exceptions/    # Custom error handling
├── Structure/     # File repositories and sorting algorithms
├── UI/            # Console interface
├── Validator/     # Input validation
├── Tests/         # Unit tests
├── main.py        # Entry point
└── *.txt          # Data files (students.txt, etc.)
