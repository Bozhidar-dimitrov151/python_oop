from collections import deque
from unittest import TestCase, main

from project_3.railway_station import RailwayStation


class RailwayStationTest(TestCase):

    def setUp(self):
        self.station = RailwayStation("Sofia")

    def test_init(self):
        self.assertEqual("Sofia", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_setter_valid_name(self):
        self.station.name = "Plovdiv"
        self.assertEqual("Plovdiv", self.station.name)

    def test_name_setter_raises_with_short_name(self):
        with self.assertRaises(ValueError) as ex:
            self.station.name = "Ab"

        self.assertEqual(
            "Name should be more than 3 symbols!",
            str(ex.exception)
        )

    def test_new_arrival_on_board(self):
        train = "Train 1"

        self.station.new_arrival_on_board(train)

        self.assertEqual(deque([train]), self.station.arrival_trains)

    def test_train_has_arrived_successfully(self):
        train = "Train 1"

        self.station.new_arrival_on_board(train)

        result = self.station.train_has_arrived(train)

        self.assertEqual(
            "Train 1 is on the platform and will leave in 5 minutes.",
            result
        )
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque([train]), self.station.departure_trains)

    def test_train_has_arrived_when_other_train_should_arrive_first(self):
        train1 = "Train 1"
        train2 = "Train 2"

        self.station.new_arrival_on_board(train1)
        self.station.new_arrival_on_board(train2)

        result = self.station.train_has_arrived(train2)

        self.assertEqual(
            "There are other trains to arrive before Train 2.",
            result
        )
        self.assertEqual(deque([train1, train2]), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_train_has_arrived_empty_queue_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.station.train_has_arrived("Train")

    def test_train_has_left_returns_true(self):
        train = "Train 1"

        self.station.new_arrival_on_board(train)
        self.station.train_has_arrived(train)

        result = self.station.train_has_left(train)

        self.assertTrue(result)

    def test_train_has_left_removes_train_from_departure_queue(self):
        train = "Train 1"

        self.station.new_arrival_on_board(train)
        self.station.train_has_arrived(train)
        self.station.train_has_left(train)

        self.assertEqual(deque(), self.station.departure_trains)

    def test_train_has_left_returns_false_when_wrong_train(self):
        train1 = "Train 1"
        train2 = "Train 2"

        self.station.new_arrival_on_board(train1)
        self.station.new_arrival_on_board(train2)

        self.station.train_has_arrived(train1)
        self.station.train_has_arrived(train2)

        result = self.station.train_has_left(train2)

        self.assertFalse(result)
        self.assertEqual(deque([train1, train2]), self.station.departure_trains)

    def test_train_has_left_returns_false_when_queue_is_empty(self):
        result = self.station.train_has_left("Train 1")

        self.assertFalse(result)


if __name__ == "__main__":
    main()