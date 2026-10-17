# Student Grade Calculator

A lightweight, terminal-based grade calculation system written in Python that allows students and teachers to calculate simple score averages, weighted course evaluations, and full-class summary performance reports.

---

## 👤 Student Information
- **Student Name:** John Maverick Rosales
- **Section:** [Insert Your Section Here, e.g., BSCS 2-A / BSIT 2-B]

---

## 📖 Program Description
The **Student Grade Calculator** is a command-line tool designed to simplify academic performance tracking. It offers three distinct evaluation modes:
1. **Simple Average Mode:** Computes the arithmetic mean of an arbitrary number of individual assignment or quiz scores.
2. **Weighted Course Grading:** Calculates the final composite grade using standard course weighting:
   - Assignments: 30%
   - Midterm Exam: 30%
   - Final Exam: 40%
3. **Batch Class Summary Statistics:** Allows educators to input grades for an entire class roster to automatically compute the class average, top performer (highest grade), lowest grade, and overall passing rate with an ASCII summary table.

Each calculation automatically assigns a standardized letter grade (`A`, `B`, `C`, `D`, `F`) and remarks (`Passed` or `Failed`). Built-in input validation prevents non-numeric entries and values outside the 0–100 scale.

---

## ⚙️ Requirements
- Python 3.7 or higher installed on your system.
- No external libraries required (uses standard library modules only).

---

## 🚀 How to Run the Program

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/grade-calculator.git
   cd grade-calculator
   ```

2. **Run the script:**
   On Windows (PowerShell / Command Prompt):
   ```powershell
   python grade_calculator.py
   ```
   On macOS / Linux:
   ```bash
   python3 grade_calculator.py
   ```

---

## 💻 Sample Program Output

```text
==================================================
          STUDENT GRADE CALCULATOR
==================================================
1. Simple Average Calculator (Single Student)
2. Weighted Course Grading (Single Student)
3. Batch Class Roster & Summary Statistics
4. Exit

Select an option (1-4): 2
Enter student name: John Maverick Rosales

Standard Weights: Assignments (30%), Midterms (30%), Finals (40%)
  Enter Assignments Average (0-100): 92
  Enter Midterm Exam Score (0-100): 88
  Enter Final Exam Score (0-100): 95

==================================================
                 GRADE REPORT
==================================================
Student:       John Maverick Rosales
Mode:          Weighted Grading
Assignments    : 92.00% (30%)
Midterm Exam   : 88.00% (30%)
Final Exam     : 95.00% (40%)
Final Grade:   92.00%
Letter Grade:  A
Remarks:       Passed (Excellent)
==================================================
```

---

## 📁 Repository Structure
```text
grade-calculator/
├── .gitignore            # Ignores Python bytecode, caches, virtual environments, and IDE files
├── grade_calculator.py   # Core Python program
└── README.md             # Project documentation and student information
```
