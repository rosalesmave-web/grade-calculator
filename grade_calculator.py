"""Student Grade Calculator.

Author: John Maverick Rosales
"""


def calculate_average(scores):
    """Calculate the simple mean average of a list of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


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


def main():
    print("=" * 45)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 45)

    student_name = input("Enter student name: ").strip()
    num_scores = int(input("Enter number of grades/scores to input: "))

    scores = []
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score #{i}: "))
        scores.append(score)

    avg = calculate_average(scores)
    letter_grade, remark = get_letter_grade(avg)

    print("\n" + "=" * 45)
    print("             GRADE REPORT")
    print("=" * 45)
    print(f"Student:       {student_name}")
    print(f"Scores:        {scores}")
    print(f"Average:       {avg:.2f}%")
    print(f"Letter Grade:  {letter_grade}")
    print(f"Status:        {remark}")
    print("=" * 45)


if __name__ == "__main__":
    main()
