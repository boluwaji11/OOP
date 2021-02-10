import StudentClass as sc

student_classification = input("Enter student classification (F,S,Jr,Sr): ")


def main():
    age = sc.Student(student_classification)

    age.agecal()
    age.regperiod()

    print()
    print("The student is", age.displayage(), "years old.")
    print()
    print(
        "The Registration period for this student classification:",
        age.displayregperiod(),
    )


main()