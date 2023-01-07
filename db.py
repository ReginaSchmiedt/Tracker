import sqlite3
from datetime import date
from prettytable import from_db_cursor
from datetime import datetime


def get_db(name="main.db"):

    """
    creates a connection to a database and creates tables in it.

    :param name: the name of the file that contains the database.
    :return: an initialized sqlite3 database connection.
    """

    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):

    """
    creates tables to store habit and checking times if they do not existe yet.

    :param db: an initialized sqlite3 database connection.
    """

    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habits (
            Name TEXT PRIMARY KEY,
            frequency TEXT, unit TEXT, creation TEXT) """)

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
         Date_Time TEXT,
         Habit_Name TEXT,
         FOREIGN KEY (habit_name) REFERENCES habits(name))""") #it takes information date and habit names and organise in columns for the check and analyse.

    db.commit()


def add_habit(db, name, frequency, unit):

    """
    adds habit to a database.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    :param frequency: how many times in a certain period the task should be executed.
    :param unit: information about the period (daily, weekly, monthly, annual)
    """

    cur = db.cursor()
    creation_date = datetime.now()
    cur.execute("INSERT INTO habits VALUES (?, ?, ?, ?)", (name, frequency, unit, creation_date))
    db.commit()



def check_habit(db, name, event_date=None):

    """
    write the date and time of habit execution in to a table of database.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    :param event_date: optional: a date and time of the habit execution.
    """

    cur = db.cursor()
    if not event_date:
        event_date = datetime.now() # date.today is a function in a library. It gives me the date of today when I use it.
    cur.execute("INSERT INTO tracker VALUES (?, ?)", (event_date, name))
    db.commit()


def get_all_habit_data(db):

    """
    creates a table that can be displayed to the user with all habits in a database.

    :param db: the name of the file that contains the database.
    :return: table for display.
    """

    cur = db.cursor() #db.cursor() creates a cursor object that it called "cur"
    #cur.execute("SELECT * FROM tracker WHERE counterName=?", (name,))
    res = cur.execute("SELECT * FROM habits")    # * it means that the object "cur" take all information from the table habits and it is saved in "res".
    mytable = from_db_cursor(cur) # the cursor has taken all the information from the table habits and the function from_db_cursor tranforms all these information in to something that can be printed as a table.
    mytable.align = "l"
    print(mytable)    #res = cur.execute("SELECT name FROM sqlite_master") #I wrote it today
    return res.fetchall()

def get_habit_data(db, name):

    """
    creates a table that can be displayed to the user with all checked data and times of a habit.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    :return: table for display.
    """

    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE Habit_Name=?", (name,))
    mytable = from_db_cursor(cur)
    mytable.align = "l"
    print(mytable)
    return cur.fetchall()

def delete_habit(db, name):

    """
    delets a habit from database.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    """

    cur = db.cursor()
    cur.execute("DELETE FROM tracker WHERE Habit_Name=?", (name,))
    cur.execute("DELETE FROM habits WHERE name=?", (name,))
    db.commit()

def update_habit(db, name, column, value):

    """
    modifies the frequency or unit of a habit.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    :param column: "frequency" or "unit".
    :param value: the new value.
    """

    if column == "frequency":
        db.execute("UPDATE habits set frequency=:freq WHERE name=:row", {"freq": value, "row": name})
    elif column == "unit":
        db.execute("UPDATE habits set unit=:unit WHERE name=:row", {"unit": value, "row": name})
    db.commit()


def get_names(db):

    """
    creates a table that can be displayed to the user with all names of habits in a database.

    :param db: the name of the file that contains the database.
    :return: table for display.
    """

    cur = db.cursor()
    res = cur.execute("SELECT Name FROM habits")    # * it means that the object "cur" take all information from the table habits and it is saved in "res".
    mytable = from_db_cursor(cur) # the cursor has taken all the information from the table habits and the function from_db_cursor tranforms all these information in to something that can be printed as a table.
    mytable.align = "l"
    print(mytable)    #res = cur.execute("SELECT name FROM sqlite_master") #I wrote it today
    return res.fetchall()

def get_sameunit(db, unit):

    """
    creates a table that can be displayed to the user with all names of habits with a given unit (daily, weekly, monthly and annual).

    :param db: the name of the file that contains the database.
    :param unit: how often the habit is executed  (daily, weekly, monthly, annual).
    :return: table for display.
    """

    cur = db.cursor()
    res = cur.execute("SELECT Name FROM habits WHERE unit=?", (unit,))    # * it means that the object "cur" take all information from the table habits and it is saved in "res".
    mytable = from_db_cursor(cur) # the cursor has taken all the information from the table habits and the function from_db_cursor tranforms all these information in to something that can be printed as a table.
    mytable.align = "l"
    print(mytable)    #res = cur.execute("SELECT name FROM sqlite_master") #I wrote it today
    return res.fetchall()

def get_checks(db, name):

    """
    creates a list of checked date and times for a given habit.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    :return: list of dates and times.
    """

    cur = db.cursor()
    res = cur.execute("SELECT Date_Time FROM tracker WHERE Habit_Name=?", (name,))
    return [x[0] for x in res.fetchall()]

def get_names_list(db):
    """
    creates a list of habit names in a database.

    :param db: the name of the file that contains the database.
    :return: list of names.
    """

    cur = db.cursor()
    res = cur.execute("SELECT Name FROM habits")    # * it means that the object "cur" take all information from the table habits and it is saved in "res".
    return [x[0] for x in res.fetchall()] #it creats a list of habit select

def get_freq_unit(db, name):
    """
    creates a list that contains the frequency and unit of a given habit from a database.

    :param db: the name of the file that contains the database.
    :param name: the name of the habit.
    :return: list that contains the frequency and unit.
    """

    cur =db.cursor()
    res = cur.execute("SELECT frequency, unit FROM habits WHERE Name=?", (name,))
    return res.fetchall()