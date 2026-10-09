def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Needs Improvement"


def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = get_grade(average)

    print("\n===== STUDENT REPORT =====")
    print(f"Total Marks : {total}")
    print(f"Average     : {average:.2f}")
    print(f"Highest     : {highest}")
    print(f"Lowest      : {lowest}")
    print(f"Grade       : {grade}")


def main():
    print("STUDENT MARKS ANALYZER")
    print("----------------------")

    name = input("Enter student name: ").strip()

    while not name:
        name = input("Name cannot be empty. Enter name: ").strip()

    while True:
        try:
            count = int(input("Number of subjects: "))
            if count > 0:
                break
            print("Enter at least one subject.")
        except ValueError:
            print("Please enter a whole number.")

    marks = []

    for i in range(count):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i + 1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Mark must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    print(f"\nStudent: {name}")
    analyze_marks(marks)


if __name__ == "__main__":
    main()