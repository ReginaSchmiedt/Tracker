from db import get_db, get_names_list, get_freq_unit, check_habit
from datetime import datetime, timedelta
from main import habit
import numpy as np
import random
from dateutil.relativedelta import relativedelta


#create five example habits
db = get_db(name="example.db")
new_habit = habit("Turn off the light when it is not needed", "1", "daily")
new_habit.store(db)
new_habit = habit("Turn off the heaters when windows are opened in the morning, afternoon and evening", "3", "daily")
new_habit.store(db)
new_habit = habit("Take public transportation instead of driving to work", "1", "daily")
new_habit.store(db)
new_habit = habit("Walk or cycle instead of driving to the gym", "3", "weekly")
new_habit.store(db)
new_habit = habit("Cut back on flying", "1", "annual")
new_habit.store(db)


habits =get_names_list(db)
for habit in habits:
    unit = get_freq_unit(db, habit)[0][1] #get_freq_unit gives a list with a tuple that has the frequency at the first position and the unit at the second.
    current_date = datetime(2022, 4, 1, 1, 1, 1)
    end_date = datetime(2022, 6, 30, 1,1 ,1)
    if unit == "daily":
        delta = timedelta(days=1)
    elif unit == "weekly":
        delta = timedelta(weeks=1)
    elif unit == "monthly":
        delta = relativedelta(months=1)
    elif unit == "annual":
        delta = relativedelta(years=1)
    while current_date <= end_date:
        is_checked = random.choices([True, False], weights=[0.7, 0.3])[0] #random is a library for random numbers and random.choices selects randoly from a list, here this list is True and False. The weights are the probabilities to choice True or False.
        if is_checked:
            check_habit(db, habit, event_date=current_date)
        current_date += delta