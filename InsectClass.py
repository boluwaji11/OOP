import random


class Insect:
    def __init__(self):
        self.__wings = 2
        self.__legs = 4
        self.__miles = 0

    # Method to determine and return the length of flight

    def flightlength(self):
        self.__miles = random.randint(1, 10)
        return self.__miles
