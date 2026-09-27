from src.data_loader import load_data
from src.analyzer import (
    calculate_average,
    add_grades_and_results,
find_top_student,
    calculate_subject_averages,
    add_rank
)


def show_all_students(students):
    print("\n===== All Students =====")

    print(
        students[
            [
                "name",
                "math",
                "science",
                "english",
                "average",
                "grade",
                "result",
                "rank"
            ]
        ].to_string(index=False)
    )


def show_top_student(students):

    top_student = find_top_student(students)

    print("\n===== Top Student =====")

    print(f"Name    : {top_student['name']}")
    print(f"Average : {top_student['average']:.2f}")
    print(f"Grade   : {top_student['grade']}")
    print(f"Rank    : {top_student['rank']}")


def search_student(students):

    name = input("\nEnter student name: ").strip()

    result = students[
        students["name"].str.lower() == name.lower()
    ]

    if result.empty:
        print("\nStudent not found.")
    else:
        print("\n===== Student Details =====")
        print(
            result[
                [
                    "name",
                    "math",
                    "science",
                    "english",
                    "average",
                    "grade",
                    "result",
                    "rank"
                ]
            ].to_string(index=False)
        )


def show_rankings(students):

    print("\n===== Student Rankings =====")

    rankings = students.sort_values("rank")

    print(
        rankings[
            [
                "rank",
                "name",
                "average",
                "grade",
                "result"
            ]
        ].to_string(index=False)
    )


def show_subject_averages(students):

    subject_averages = calculate_subject_averages(students)

    print("\n===== Subject Averages =====")

    for subject, average in subject_averages.items():
        print(f"{subject.capitalize():10} : {average:.2f}")


def show_pass_fail_statistics(students):

    total_students = len(students)

    passed = len(students[students["result"] == "Pass"])
    failed = len(students[students["result"] == "Fail"])

    pass_percentage = (passed / total_students) * 100
    fail_percentage = (failed / total_students) * 100

    print("\n===== Pass/Fail Statistics =====")

    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    print(f"Pass Percentage: {pass_percentage:.2f}%")
    print(f"Fail Percentage: {fail_percentage:.2f}%")


def display_menu():

    print("\n")
    print("========================================")
    print("      STUDENT PERFORMANCE ANALYZER")
    print("========================================")
    print("1. View all students")
    print("2. Search student")
    print("3. View top student")
    print("4. View rankings")
    print("5. Subject analysis")
    print("6. Pass/Fail statistics")
    print("7. Exit")
    print("========================================")


def main():

    file_path = "data/students.csv"
    students = load_data(file_path)


    students = calculate_average(students)
    students = add_grades_and_results(students)
    students = add_rank(students)


    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_all_students(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            show_top_student(students)

        elif choice == "4":
            show_rankings(students)

        elif choice == "5":
            show_subject_averages(students)

        elif choice == "6":
            show_pass_fail_statistics(students)

        elif choice == "7":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()