from counter import Counter
from db import get_db, add_counter, increment_counter


class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")

        add_counter(self.db, "test_counter", "test_description")
        increment_counter(self.db, "test_counter", "2022-12-06")
        increment_counter(self.db, "test_counter", "2022-12-07")

        increment_counter(self.db, "test_counter", "2022-12-09")
        increment_counter(self.db, "test_counter", "2022-12-10")

    def test_counter(self):
        counter = Counter("test_counter_1", "test_description_1")
        counter.store(self.db)

        counter.increment()
        counter.add_event(self.db)
        counter.reset()
        counter.increment()

    def teardown_method(self):
        import os
        os.remove("test.db")
