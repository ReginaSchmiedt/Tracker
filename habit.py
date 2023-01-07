from db import add_habit
from datetime import datetime

class habit:

    """
    class habit:
    A class used to represent habits
    ...
    Attributes
    ----------
    name: str
        the name of the habit
    frequency: str
        how many times the user did an activity
    unit: str
        the unit or period of the frequency that the user does a habit (daily, weekly, monthly or annual)

    """

    def __init__(self, name, frequency, unit): #attributes
        self.name = str(name)
        self.frequency = str(frequency)
        self.unit = str(unit)
        self.checks = []

    def check(self):
        self.checks.append(datetime.now())

    def store(self, db):
        add_habit(db, self.name, self.frequency, self.unit)

