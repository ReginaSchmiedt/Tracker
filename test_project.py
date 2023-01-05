from habit import habit
from db import get_db, get_habit_data, add_habit, get_all_habit_data, check_habit, delete_habit, update_habit, get_names, get_sameunit, get_names_list
from analyse import longest_streak_of_habit, longest_streak_of_all



class TestTrackHabit:

    def setup_method(self):
        self.db = get_db("test.db")
        habit_name = "Test_habit"
        frequency_habit = "three",  # 3 times per day
        unit = "daily"
        new_habit = habit(habit_name, frequency_habit, unit)
        new_habit.store(self.db)
        check_habit(self.db, "Test_habit", event_date="2022-12-15 22:16:10")
        check_habit(self.db, "Test_habit", event_date="2022-12-16 22:16:10")
        check_habit(self.db, "Test_habit", event_date="2022-12-17 22:16:10")
        check_habit(self.db, "Test_habit", event_date="2022-12-18 22:16:10")
        check_habit(self.db, "Test_habit", event_date="2022-12-19 22:16:10")


        # add_counter(self.db, "test_counter", "test_description")
        # increment_counter(self.db, "test_counter", "2022-12-06")
        # increment_counter(self.db, "test_counter", "2022-12-07")
        #
        # increment_counter(self.db, "test_counter", "2022-12-09")
        # increment_counter(self.db, "test_counter", "2022-12-10")

    def test_habit(self):
        habits = habit("test_habit_1", 3, "daily")
        habits.store(self.db)

        habits.check()
        # counter.add_event(self.db)
        # counter.reset()
        # counter.increment()

    def teardown_method(self):
        import os
        os.remove("test.db")
