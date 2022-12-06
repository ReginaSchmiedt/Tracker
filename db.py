import sqlite3
from datetime import date
from prettytable import from_db_cursor


def get_db(name="main.db"):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    cur = db.cursor()

    # cur.execute("""CREATE TABLE IF NOT EXISTS counter (
    #     name TEXT PRIMARY KEY,
    #     description TEXT,
    #     unit TEXT) """)

    cur.execute("""CREATE TABLE IF NOT EXISTS habits (
            name TEXT PRIMARY KEY,
            frequency TEXT,            unit TEXT) """)

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
         date TEXT,
         habitName TEXT,
         FOREIGN KEY (habitName) REFERENCES habits(name))""") #it takes information date and habit names and organise in columns for the check and analyse.

    db.commit()


# def add_counter(db, name, description): #we are not using this
#     cur = db.cursor()
#     cur.execute("INSERT INTO counter VALUES (?, ?)", (name, description))
#     db.commit()


def add_habit(db, name, frequency, unit):
    cur = db.cursor()
    cur.execute("INSERT INTO habits VALUES (?, ?, ?)", (name, frequency, unit))
    db.commit()


# def increment_counter(db, name, event_date=None): #we are not using this. I am keeping this as example.
#     cur = db.cursor()
#     if not event_date:
#         event_date = date.today()
#     cur.execute("INSERT INTO Tracker VALUES (?, ?)", (event_date, name))
#     db.commit()

def check_habit(db, name, event_date=None):
    cur = db.cursor()
    if not event_date:
        event_date = date.today() # date.today is a function in a library. It gives me the date of today when I use it.
    cur.execute("INSERT INTO tracker VALUES (?, ?)", (event_date, name))
    db.commit()


# def get_counter_data(db, name):#we are not using this
#     cur = db.cursor()
#     cur.execute("SELECT * FROM tracker WHERE counterName=?", (name,))
#     return cur.fetchall()


# def get_habit_data(db): # maybe we are going to use this later
#     cur = db.cursor()
#     cur.execute("SELECT * FROM tracker WHERE counterName=?", (name,))
#     return cur.fetchall()


def get_all_habit_data(db):#editei isso
    cur = db.cursor() #db.cursor() creates a cursor object that it called "cur"
    #cur.execute("SELECT * FROM tracker WHERE counterName=?", (name,))
    res = cur.execute("SELECT * FROM habits")    # * it means that the object "cur" take all information from the table habits and it is saved in "res".
    mytable = from_db_cursor(cur) # the cursor has taken all the information from the table habits and the function from_db_cursor tranforms all these information in to something that can be printed as a table.
    mytable.align = "l"
    print(mytable)    #res = cur.execute("SELECT name FROM sqlite_master") #I wrote it today
    return res.fetchall()

def get_habit_data(db, name):#we are not using this
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE habitName=?", (name,))
    mytable = from_db_cursor(cur)
    mytable.align = "l"
    print(mytable)
    return cur.fetchall()