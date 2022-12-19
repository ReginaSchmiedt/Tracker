import datetime
from db import get_checks, get_names, get_names_list, get_freq_unit
import pandas as pd



def streak_lenght(db, name):
    check_list = get_checks(db, name)
    print(check_list)

    list_names = get_names_list(db) #I am defining a variable and calling the function
    print(get_names_list(db))
    for habit in list_names:
        check_list = get_checks(db, habit)
        print(check_list)
        #date_time_obj = datetime.strptime(date_time_str, '%y%m/%d %H:%M:%S')
        date_time_list = [datetime.datetime.strptime(date_time_str[:-7], '%Y-%m-%d %H:%M:%S') for date_time_str in check_list]
        """here the for loop takes the str inside of the checkslist and the function "datetime.datetime.strptime" 
        converts them to datetime. """

        print(get_freq_unit(db, habit))


        unit = get_freq_unit(db, habit)[0][1]


        streak_ID_list = [1]

        for i in range(1, len(date_time_list)):
            if unit == "daily":
                if (date_time_list[i] - date_time_list[i - 1]).days < 2:
                    streak_ID_list.append(streak_ID_list[i - 1])
                else:
                    streak_ID_list.append(streak_ID_list[i - 1] + 1)

            elif unit == "weekly":
                if (date_time_list[i] - date_time_list[i - 1]).weeks < 2:
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

        streaks = pd.Series(streak_ID_list, name='streak_id').to_frame()
        streaks = streaks.append({'checks': date_time_list}, ignore_index=True)
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
        print(streaks)
        #
        # streak_length = streaks['streak_counter']
        # print(streak_length)

        print(streak_ID_list)


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