from db import get_counter_data

def calculate_count(db, counter):
    """
    Calculate the counter of the counter.

    :param db: an initialized sqlite3 database connection
    :param counter: name of the counter present in DB
    :return: length of the counter increment events
    """

    data = get_counter_data(db, counter)
    return len(data)