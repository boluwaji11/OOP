import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.miles = 0

    def flightlength(self):
        self.miles = random.randint(1, 10)

    def display(self):
        return self.miles
