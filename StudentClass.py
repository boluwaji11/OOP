import datetime


class Student:
    def __init__(self, stdID, name, dob, classification):
        self.__classification = classification
        self.__studentid = stdID
        self.__name = name
        self.__dob = dob
        self.__age = 0
        self.__period = 0

    def agecal(self):
        # Extract year from DOB and convert to an integer
        student_year = int(self.__dob[6:])

        # Calculate the age
        self.__age = datetime.date.today().year - student_year
        return self.__age

    def regperiod(self):
        if self.__classification == "F":
            self.__period = "Freshmen - 11/10 thru 11/12"
        elif self.__classification == "S":
            self.__period = "Sophomores – 11/7 thru 11/9"
        elif self.__classification == "Jr":
            self.__period = "Juniors – 11/4 thru 11/6"
        elif self.__classification == "Sr":
            self.__period = "Seniors – 11/1 thru 11/3"
        else:
            self.__period = "Invalid Classification"
        return self.__period
