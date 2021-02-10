import datetime


class Student:
    def __init__(self, classification):
        self.classification = classification
        self.studentid = "1234"
        self.name = "Bolu"
        self.dob = "04/11/2004"
        self.age = 0
        self.period = 0

    def agecal(self):
        # Extract year from DOB and convert to an integer
        student_year = int(self.dob[6:])

        # Calculate the age
        self.age = datetime.date.today().year - student_year

    def regperiod(self):
        if self.classification == "F":
            self.period = "Freshmen - 11/10 thru 11/12"
        elif self.classification == "S":
            self.period = "Sophomores – 11/7 thru 11/9"
        elif self.classification == "Jr":
            self.period = "Juniors – 11/4 thru 11/6"
        elif self.classification == "Sr":
            self.period = "Seniors – 11/1 thru 11/3"
        else:
            self.period = "Invalid Classification"

    def displayage(self):
        return self.age

    def displayregperiod(self):
        return self.period
