import questionary
import datetime
from db import get_db, get_habit_data, add_habit, get_all_habit_data, check_habit, delete_habit, update_habit, get_names, get_sameunit, get_names_list
from analyse import longest_streak_of_habit, longest_streak_of_all
from habit import habit

#from analyse import calculate_streak

#ToDo:
#predefined habit: For each predefined habit, provide example tracking data for a period of 4 weeks.
#Analyse: Return the longest run streak of all defined habits; Return the longest run streak for a given habit.
#Prof. Max: please make sure to write unit tests for your solution and add the four weeks of test data with which you can demonstrate that your streak calculation works.



"""
-class habit:
A class used to represent habits

-Attributes:
............
name: str
the name of the habit
frequency: str
how many times the user did an activity
unit: str
the unit or period of the frequency that the user does a habit (daily, weekly, monthly or annual)

"""
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


def cli():
    db = get_db(name="example.db") #conecting to example.db
    question = questionary.confirm("Hello, you are welcome! Are you ready?").ask()
    """
    First step: the system welcome the user.
    """
    if not question:
        quit()


    stop = False
    while not stop:
        choice = questionary.select(
            "What do you what to do?",
            choices=["Create", "Manage", "Analyse", "Exit"]
        ).ask()
        """
        Second step: The system ask the user what he wants to do.
        While using the user interface of the habit tracker, the user can use the arrow keys to move to an option and then select it with ENTER.
.
        """


        if choice == "Create":
            option = questionary.select(
                "What do you what to do?",
                choices=["Predefined", "Define", "Exit"]
            ).ask()

            """
            To get used with the system, the user has the option to first use “Predefined habits” to learn how to use the system. Then later, he can “Create” his own habits that he wants to track.
            """
            if option == "Predefined":
                """The system comes with 5 predefined habits"""
                selection = questionary.select(
                    "What do you what to do?",

                    choices=["1 - Turn off the light when it is not needed.",
                             "2 - Turn off the heaters when windows are opened in the morning, afternoon and evening.",
                             "3 - Take public transportation instead of driving to work.",
                             "4 - Walk or cycle instead of driving to the gym.",
                             "5 - Cut back on flying."]
                ).ask()
                if selection == "1 - Turn off the light when it is not needed.":

                    habit_name = "1 - Turn off the light when it is not needed."
                    frequency_habit = "three", #3 times per day
                    unit = "daily"
                    new_habit = habit(habit_name, frequency_habit, unit)
                    new_habit.store(db)

                    """
                    The system offers a list of predefined habits. The user needs to choose from this list the habits he wants to track.
                    Frequency = how often you want to do the task per period (unit). It should be in numbers.
                    Unit = The periodicity of the habit (daily, weekly, monthly or annually).
                    """

                elif selection == '2 - Turn off the heaters when windows are opened in the morning, afternoon and evening.':
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

                elif selection == "5 - Cut back on flying.":
                    habit_name = "5 - Cut back on flying."
                    frequency_habit = "once",  # once per year
                    unit = "annual"
                    new_habit = habit(habit_name, frequency_habit, unit)
                    new_habit.store(db)

                pass


            elif option == "Define":
                habit_name = input("Enter the name of your habit: ")
                frequency_habit = input("Enter the frequency of your habit: ")
                unit = input("Enter the unit of your habit (daily, weekly, monthly or annual): ")
                new_habit = habit(habit_name, frequency_habit, unit)
                new_habit.store(db)

                pass
                """
                The user can creates his own habits to track by typing the name of the habits by input from the keyboard. He can also choose how often he wants to do the task per period (unit). It should be in numbers.
                """

            else:
                print("Bye")
                stop = True

                """ The user can leave the app any time. """

#Here the user can check, edit or delete habits
        elif choice == "Manage":
            option = questionary.select(
                "What do you what to do?",
                choices=["Check", "Edit", "Delete", "Exit"]
            ).ask()

            """ 
            The user has the option to manage his habits. In this case, he can choose if he wants to see and check the habits that you are tracking;
            But, if he is a little behind schedule, he can make necessary adjustments by the option "edit";
            Besides, If he has difficult time achieving any of his goals from his habit list, he has also the option to delete a habit anytime and then focus on those that matter the most to him at that moment.
            """
            if option == "Check":
                # enter the date and time
                #print(get_all_habit_data(db, "name", "frequency", "unit"), "\n") # this function is not correct. I need a function that give me a list with all names of habits that the user creats. This function should be defined in the db.py and called at main.py (here).

                get_all_habit_data(db)
                get_habit_name = input("Enter the name of the habit you want to check: ")
                check_habit(db, get_habit_name)
                pass


            elif option == "Edit":
                get_all_habit_data(db)
                get_habit_name = input("Enter the name of the habit you want to edit: ")
                choose_frequency_unit = input("Enter what you want to edit: frequency or unit: ")
                new_value = input("Enter the new value: ")
                update_habit(db, get_habit_name, choose_frequency_unit, new_value)
                pass


            elif option == "Delete":
                get_all_habit_data(db)
                get_habit_name = input("Enter the name of the habit you want to delete: ")

                delete_habit(db, get_habit_name)

# The user can delete habits. 
                pass

            else:
                print("Bye")
                stop = True

# The system offers to the user the option “Analyze”, to evaluate his progress.

        elif choice == "Analyse":
            option_analysis = questionary.select(
                "What do you what to do?",
                choices=["1. Currently tracked habits", "2. Habits with the same periodicity", "3. Longest run streak of all defined habits", "4. Longest run streak for a given habit", "Exit"]
            ).ask()

            if option_analysis == "1. Currently tracked habits":
                currently_habits = get_names(db)
                pass


            elif option_analysis == "2. Habits with the same periodicity":
                option_sameunit = questionary.select(
                    "What do you what to do?",
                    choices=["daily", "weekly", "monthly", "annual", "Exit"]
                ).ask()

                if option_sameunit == "daily":
                    same_unit = get_sameunit(db, option_sameunit)
                    pass
                elif option_sameunit == "weekly":
                    same_unit = get_sameunit(db, option_sameunit)

                elif option_sameunit == "monthly":
                    same_unit = get_sameunit(db, option_sameunit)

                elif option_sameunit == "annual":
                    same_unit = get_sameunit(db, option_sameunit)


            elif option_analysis == "3. Longest run streak of all defined habits":
                print(longest_streak_of_all(db))
                pass


            elif option_analysis == "4. Longest run streak for a given habit":
                what_habit = questionary.select(
                    "Which habit",
                    choices=get_names_list(db)
                ).ask()
                print("Longest streak:", longest_streak_of_habit(db, what_habit))
                pass


        else:
            print("Bye!")
            stop = True


if __name__ == '__main__':
    cli()


