import StudentClass as sc


def main():

    studentID = input("Enter student ID: ")
    name = input("Enter name: ")
    dob = input("Enter dob in DD/MM/YYYY format: ")
    student_classification = input("Enter student classification (F,S,Jr,Sr): ")

    age = sc.Student(studentID, name, dob, student_classification)

    print()
    print("The student is", age.agecal(), "years old.")
    print()
    print(
        "The Registration period for this student classification:",
        age.regperiod(),
    )


main()