import questionary
import datetime
from db import get_db, get_habit_data, add_habit, get_all_habit_data, check_habit
#from counter import Counter
from habit import habit
#from analyse import calculate_count


# """
# class habit:
# A class used to represent habits
# ...
# Attributes
# ----------
# name: str
#     the name of the habit
# frequency: str
#     how many times the user did an activity
# unit: str
#     the unit or period of the frequency that the user does a habit (daily, weekly, monthly or annual)
#
# """
# class habit:
#     def __init__(self, name, frequency, unit): #attributes
#         self.name = str(name)
#         self.frequency = str(frequency)
#         self.unit = str(unit)
#         self.checks = []
#
#     def check(self):
#         self.checks.append(datetime.date.today())
#
#     def store(self, db):
#         add_habit(db, self.name, self.frequency, self.unit)

# First step:
def cli():
    db = get_db()
    question = questionary.confirm("Hello, you are welcome! Are you ready?").ask()
    if not question:
        quit()

# Second step: The user can choose what he wants to do.
    stop = False
    while not stop:
        choice = questionary.select(
            "What do you what to do?",
            choices=["Create", "Manage", "Analyse", "Exit"]
        ).ask()

#name = questionary.text("What is the name of your counter?").ask() I can remove it

# To get used with the system, the user has the option to first use “Predefined habits” and then later “Create” his own habits that he wants to track.
        if choice == "Create":
            option = questionary.select(
                "What do you what to do?",
                choices=["Predefined", "Define", "Exit"]
            ).ask()
            if option == "Predefined":
                selection = questionary.select(
                    "What do you what to do?",

                    choices=["1 - Turn off the light when it is not needed.",
                             "2 - Turn off the heaters when windows are opened in the morning, afternoon and evening.",
                             "3 - Take public transportation instead of driving to work.",
                             "4 - Walk or cycle instead of driving to the gym."]
                ).ask()
                if selection == "1 - Turn off the light when it is not needed.":

                    habit_name = "1 - Turn off the light when it is not needed."
                    frequency_habit = "three", #3 times per day
                    unit = "daily"
                    new_habit = habit(habit_name, frequency_habit, unit)
                    new_habit.store(db)

                elif selection == "2 - Turn off the heaters when windows are opened in the morning, afternoon and evening.":
                    habit_name = "2 - Turn off the heaters when windows are opened in the morning, afternoon and evening."
                    frequency_habit = "three",  # 3 times per day
                    unit = "daily"
                    new_habit = habit(habit_name, frequency_habit, unit)
                    new_habit.store(db)

                elif selection == "3 - Take public transportation instead of driving to work.":
                    habit_name = "3 - Take public transportation instead of driving to work."
                    frequency_habit = "one",  # once per day
                    unit = "daily"
                    new_habit = habit(habit_name, frequency_habit, unit)
                    new_habit.store(db)

                elif selection == "4 - Walk or cycle instead of driving to the gym.":
                    habit_name = "4 - Walk or cycle instead of driving to the gym."
                    frequency_habit = "three",  # 3 times per week
                    unit = "weekly"
                    new_habit = habit(habit_name, frequency_habit, unit)
                    new_habit.store(db)

                pass

# Here the user can create his own habits to track.
            elif option == "Define":

                habit_name = input("Enter the name of your habit: ")
                frequency_habit = input("Enter the frequency of your habit: ")
                unit = input("Enter the unit of your habit (daily, weekly, monthly or annual): ")
                new_habit = habit(habit_name, frequency_habit, unit)
                new_habit.store(db)

                pass
# The user can leave the app any time
            else:
                print("Bye")
                stop = True

#Here the user can check, edit or delete habits
        elif choice == "Manage":
            option = questionary.select(
                "What do you what to do?",
                choices=["Check", "Edit", "Delete", "Exit"]
            ).ask()
            if option == "Check":
                # enter the date and time
                #print(get_all_habit_data(db, "name", "frequency", "unit"), "\n") # this function is not correct. I need a function that give me a list with all names of habits that the user creats. This function should be defined in the db.py and called at main.py (here).

                get_all_habit_data(db)
                get_habit_name = input("Enter the name of the habit you want to check: ")
                check_habit(db, get_habit_name)

                pass
            elif option == "Edit":
# The user can edit the periodicity habits: daily, weekly, monthly.
                pass

            elif option == "Delete":
# The user can delete habits.
                pass

            else:
                print("Bye")
                stop = True

# The system offers to the user the option “Analyze”, to evaluate his progress.

        elif choice == "Analyse":
            get_all_habit_data(db)
            get_habit_name = input("Enter the name of the habit you want to display: ")
            get_habit_data(db, get_habit_name)
# Table that show all the analyses
            pass


        #     desc = questionary.text("what is the description of your counter?").ask()
        #     counter = Counter(name, desc)
        #     counter.store(db)
        # elif choice == "manage":
        #     counter = Counter(name, "no description")
        #     counter.increment()
        #     counter.add_event(db)
        # elif choice == "analyse":
        #     count = calculate_count(db, name)
        #     print(f"f{name} has been managed {count} times")
        else:
            print("Bye!")
            stop = True


if __name__ == '__main__':
    cli()
