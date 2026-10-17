"""Student Grade Calculator.

Author: John Maverick Rosales
Features:
- Simple Average Grading
- Weighted Course Grading (Assignments 30%, Midterms 30%, Finals 40%)
- Batch Student Processing with Class Summary Statistics
"""


def get_valid_float(prompt, min_val=0.0, max_val=100.0):
    """Prompt user repeatedly until a valid float within [min_val, max_val] is provided."""
    while True:
        try:
            val = float(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"Error: Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid numerical number.")


def get_valid_int(prompt, min_val=1, max_val=100):
    """Prompt user repeatedly until a valid integer within [min_val, max_val] is provided."""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"Error: Value must be an integer between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


def calculate_simple_average(scores):
    """Calculate the simple mean average of a list of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def calculate_weighted_average(components):
    """Calculate weighted grade from component tuples: (score, weight_percent)."""
    total_weight = sum(weight for _, weight in components)
    if total_weight == 0:
        return 0.0
    weighted_sum = sum(score * (weight / 100.0) for score, weight in components)
    return (weighted_sum / total_weight) * 100.0 if total_weight != 100.0 else weighted_sum


def get_letter_grade(score):
    """Convert a numeric percentage into a letter grade and remarks."""
    if score >= 90:
        return "A", "Passed (Excellent)"
    elif score >= 80:
        return "B", "Passed (Very Good)"
    elif score >= 70:
        return "C", "Passed (Satisfactory)"
    elif score >= 60:
        return "D", "Passed (Needs Improvement)"
    else:
        return "F", "Failed"


def display_report_card(student_name, mode_name, final_score, details=None):
    letter, remark = get_letter_grade(final_score)
    print("\n" + "=" * 50)
    print("                 GRADE REPORT")
    print("=" * 50)
    print(f"Student:       {student_name}")
    print(f"Mode:          {mode_name}")
    if details:
        for k, v in details.items():
            print(f"{k:<15}: {v}")
    print(f"Final Grade:   {final_score:.2f}%")
    print(f"Letter Grade:  {letter}")
    print(f"Remarks:       {remark}")
    print("=" * 50)


def run_simple_mode():
    student_name = input("Enter student name: ").strip() or "Anonymous Student"
    num_scores = get_valid_int("Enter number of scores to record (1-50): ", min_val=1, max_val=50)

    scores = []
    for i in range(1, num_scores + 1):
        score = get_valid_float(f"  Enter score #{i} (0-100): ")
        scores.append(score)

    final_score = calculate_simple_average(scores)
    display_report_card(student_name, "Simple Average", final_score, {"Scores": scores})


def run_weighted_mode():
    student_name = input("Enter student name: ").strip() or "Anonymous Student"
    print("\nStandard Weights: Assignments (30%), Midterms (30%), Finals (40%)")

    assignments = get_valid_float("  Enter Assignments Average (0-100): ")
    midterm = get_valid_float("  Enter Midterm Exam Score (0-100): ")
    finals = get_valid_float("  Enter Final Exam Score (0-100): ")

    components = [
        (assignments, 30.0),
        (midterm, 30.0),
        (finals, 40.0)
    ]

    final_score = calculate_weighted_average(components)
    details = {
        "Assignments": f"{assignments:.2f}% (30%)",
        "Midterm Exam": f"{midterm:.2f}% (30%)",
        "Final Exam": f"{finals:.2f}% (40%)"
    }
    display_report_card(student_name, "Weighted Grading", final_score, details)


def run_batch_summary_mode():
    """Process multiple students and display class statistics."""
    num_students = get_valid_int("Enter number of students in class (1-100): ", min_val=1, max_val=100)
    roster = []

    for i in range(1, num_students + 1):
        print(f"\n--- Student #{i} ---")
        name = input("Student Name: ").strip() or f"Student #{i}"
        final_grade = get_valid_float(f"Enter Final Numeric Grade for {name} (0-100): ")
        letter, remark = get_letter_grade(final_grade)
        roster.append({"name": name, "grade": final_grade, "letter": letter, "remark": remark})

    grades = [s["grade"] for s in roster]
    class_avg = sum(grades) / len(grades)
    highest = max(roster, key=lambda s: s["grade"])
    lowest = min(roster, key=lambda s: s["grade"])
    passed_count = sum(1 for s in roster if s["letter"] != "F")

    print("\n" + "=" * 65)
    print("                    CLASS GRADE SUMMARY")
    print("=" * 65)
    print(f"{'Student Name':<25} | {'Grade':<8} | {'Letter':<7} | {'Status'}")
    print("-" * 65)
    for s in roster:
        print(f"{s['name']:<25} | {s['grade']:>6.2f}% | {s['letter']:<7} | {s['remark']}")
    print("=" * 65)
    print(f"Total Students:   {len(roster)}")
    print(f"Class Average:    {class_avg:.2f}%")
    print(f"Highest Grade:    {highest['name']} ({highest['grade']:.2f}%)")
    print(f"Lowest Grade:     {lowest['name']} ({lowest['grade']:.2f}%)")
    print(f"Passing Rate:     {(passed_count / len(roster)) * 100:.1f}% ({passed_count}/{len(roster)} passed)")
    print("=" * 65)


def main():
    while True:
        print("\n" + "=" * 50)
        print("          STUDENT GRADE CALCULATOR")
        print("=" * 50)
        print("1. Simple Average Calculator (Single Student)")
        print("2. Weighted Course Grading (Single Student)")
        print("3. Batch Class Roster & Summary Statistics")
        print("4. Exit")
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            run_simple_mode()
        elif choice == "2":
            run_weighted_mode()
        elif choice == "3":
            run_batch_summary_mode()
        elif choice == "4":
            print("\nThank you for using Student Grade Calculator! Goodbye.")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
