import datetime
from db import get_checks, get_names, get_names_list, get_freq_unit
import pandas as pd
import numpy as np



def longest_streak_of_habit(db, habit):
    check_list = get_checks(db, habit)

    date_time_list = [datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S') for date_time_str in
                      check_list]
    """here the for loop takes the str inside of the checkslist and the function "datetime.datetime.strptime" 
    converts them to datetime. """

    unit = get_freq_unit(db, habit)[0][1]


    streak_ID_list = [1]

    for i in range(1, len(check_list)):
        if unit == "daily":
            if (date_time_list[i] - date_time_list[i - 1]).days < 2:
                streak_ID_list.append(streak_ID_list[i - 1])
            else:
                streak_ID_list.append(streak_ID_list[i - 1] + 1)

        elif unit == "weekly":
            if (date_time_list[i] - date_time_list[i - 1]).days < 8:
                streak_ID_list.append(streak_ID_list[i - 1])
            else:
                streak_ID_list.append(streak_ID_list[i - 1] + 1)

        elif unit == "monthly":
            if (date_time_list[i] - date_time_list[i - 1]).months < 2:
                streak_ID_list.append(streak_ID_list[i - 1])
            else:
                streak_ID_list.append(streak_ID_list[i - 1] + 1)

        elif unit == "annual":
            if (date_time_list[i] - date_time_list[i - 1]).years < 2:
                streak_ID_list.append(streak_ID_list[i - 1])
            else:
                streak_ID_list.append(streak_ID_list[i - 1] + 1)
    streaks_list = [check_list, streak_ID_list]
    streaks_list = list(zip(*streaks_list))
    streaks = pd.DataFrame(streaks_list, columns=["checks", "streak_id"])
    streaks['streak_counter'] = streaks.groupby('streak_id').cumcount() + 1
    streaks['start_of_streak'] = streaks['streak_counter'] == 1
    streaks['end_of_streak'] = streaks['start_of_streak'].shift(-1, fill_value=True)
    streaks.loc[streaks['start_of_streak'], 'start_streak'] = streaks['checks']
    streaks['start_streak'] = streaks['start_streak'].fillna(method="ffill")
    streaks = streaks[streaks['end_of_streak']]
    streaks = streaks.rename({
        "checks": "end_streak",
        "streak_counter": "streak_length"
    }, axis=1)
    cols = ["streak_length", "start_streak", "end_streak"]
    streaks = streaks[cols]
    streak_lengths_array = streaks["streak_length"].values
    longest_streak_index =np.argmax(streak_lengths_array)
    return_value = {"streak_start": streaks["start_streak"].values[longest_streak_index],
                    "streak_end": streaks["end_streak"].values[longest_streak_index],
                    "length": streaks["streak_length"].values[longest_streak_index]}
    return return_value

def longest_streak_of_all(db):
    list_names = get_names_list(db)  # I am defining a variable and calling the function
    streak_lengths = []
    streaks_start_end = []
    for habit in list_names:
        longest = longest_streak_of_habit(db, habit)
        streak_lengths.append(longest['length'])
        streaks_start_end.append((longest['streak_start'],
                                  longest['streak_end']))
    longest_all = np.argmax(np.array(streak_lengths))
    return {'habit': list_names[longest_all], 'streak_start': streaks_start_end[longest_all][0], 'streak_end': streaks_start_end[longest_all][1], 'length':
            streak_lengths[longest_all]}
    #
    # streak_length = streaks['streak_counter']
    # print(streak_length)




#ToDo:
# write a function that take all names of all habits and put them into a list.DONE!
#Then with a loop we can go through this list.DONE!
#And read the checks of each habit.DONE!
# From this checks we calculate the streaks lengths and find the longest one. THIS WE NEED TO DO

# from db import get_counter_data
#
# def calculate_count(db, counter):
#     """
#     Calculate the counter of the counter.
#
#     :param db: an initialized sqlite3 database connection
#     :param counter: name of the counter present in DB
#     :return: length of the counter increment events
#     """
#
#     data = get_counter_data(db, counter)
#     return len(data)