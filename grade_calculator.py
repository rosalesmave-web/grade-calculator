"""Student Grade Calculator - Base CLI Implementation.

Author: John Maverick Rosales
"""


def calculate_average(scores):
    """Calculate the simple mean average of a list of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


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

    print("\n" + "-" * 45)
    print(f"Student: {student_name}")
    print(f"Scores entered: {scores}")
    print(f"Average Score: {avg:.2f}%")
    print("-" * 45)


if __name__ == "__main__":
    main()
