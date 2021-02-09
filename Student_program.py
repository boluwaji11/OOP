import StudentClass as sc


def main():
    age = sc.Student()

    age.agecal()
    age.regperiod()

    print("The student is", age.displayage(), "years old.")
    print()
    print("The Registration period for each classification:", age.displayregperiod())


main()