"""Student Grade Calculator.

Author: John Maverick Rosales
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
        return "D", "Passed (Conditional / Needs Improvement)"
    else:
        return "F", "Failed"


def run_simple_mode():
    student_name = input("Enter student name: ").strip() or "Anonymous Student"
    num_scores = get_valid_int("Enter number of scores to record (1-50): ", min_val=1, max_val=50)

    scores = []
    for i in range(1, num_scores + 1):
        score = get_valid_float(f"  Enter score #{i} (0-100): ")
        scores.append(score)

    final_score = calculate_simple_average(scores)
    letter, remark = get_letter_grade(final_score)

    print("\n" + "=" * 45)
    print("             GRADE REPORT")
    print("=" * 45)
    print(f"Student:       {student_name}")
    print(f"Mode:          Simple Average")
    print(f"Scores:        {scores}")
    print(f"Final Grade:   {final_score:.2f}%")
    print(f"Letter Grade:  {letter}")
    print(f"Remarks:       {remark}")
    print("=" * 45)


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
    letter, remark = get_letter_grade(final_score)

    print("\n" + "=" * 45)
    print("             GRADE REPORT")
    print("=" * 45)
    print(f"Student:       {student_name}")
    print(f"Mode:          Weighted Grading")
    print(f"Assignments:   {assignments:.2f}% (30%)")
    print(f"Midterm Exam:  {midterm:.2f}% (30%)")
    print(f"Final Exam:    {finals:.2f}% (40%)")
    print(f"Final Grade:   {final_score:.2f}%")
    print(f"Letter Grade:  {letter}")
    print(f"Remarks:       {remark}")
    print("=" * 45)


def main():
    print("=" * 50)
    print("          STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print("1. Simple Average Calculator")
    print("2. Weighted Course Grading (30% / 30% / 40%)")
    choice = input("\nSelect grading mode (1 or 2): ").strip()

    if choice == "2":
        run_weighted_mode()
    else:
        run_simple_mode()


if __name__ == "__main__":
    main()
