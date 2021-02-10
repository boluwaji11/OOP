import StudentClass as sc


def main():
    student_classification = input("Enter student classification (F,S,Jr,Sr): ")

    age = sc.Student(student_classification)

    print()
    print("The student is", age.agecal(), "years old.")
    print()
    print(
        "The Registration period for this student classification:",
        age.regperiod(),
    )


main()