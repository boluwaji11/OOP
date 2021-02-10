import datetime


class Student:
    def __init__(self):
        self.studentid = "1234"
        self.name = "Bolu"
        self.dob = "04/11/2004"
        self.classification = "F, S, Jr, Sr"
        self.age = 0
        self.period = 0

    def agecal(self):
        # Extract year from DOB and convert to an integer
        student_year = int(self.dob[6:])

        # Calculate the age
        self.age = datetime.date.today().year - student_year

    def regperiod(self):
        self.period = "\nSeniors – 11/1 thru 11/3 \nJuniors – 11/4 thru 11/6 \nSophomores – 11/7 thru 11/9 \nFreshmen – 11/10 thru 11/12"

    def displayage(self):
        return self.age

    def displayregperiod(self):
        return self.period
