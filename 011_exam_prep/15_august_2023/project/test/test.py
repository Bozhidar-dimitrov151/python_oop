from project.trip import Trip
from unittest import TestCase, main

class TripTest(TestCase):
    def test_init(self):
        t1 = Trip(1000, 1, False)
        t2 = Trip(1000, 2, False)
        t3 = Trip(1000, 2, True)

        self.assertEqual(t1.budget, 1000.0)
        self.assertEqual(t1.travelers, 1)
        self.assertFalse(t1.is_family)
        self.assertEqual(t1.booked_destinations_paid_amounts, {})

        self.assertEqual(t1.budget, 1000.0)
        self.assertEqual(t2.travelers, 2)
        self.assertFalse(t2.is_family)
        self.assertEqual(t2.booked_destinations_paid_amounts, {})

        self.assertEqual(t3.budget, 1000.0)
        self.assertEqual(t3.travelers, 2)
        self.assertTrue(t3.is_family)
        self.assertEqual(t3.booked_destinations_paid_amounts, {})

    def test_0_travelers_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = Trip(500, 0, False)
        self.assertEqual(str(ve.exception), "At least one traveler is required!")

    def test_negative_travelers_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = Trip(500, -1, False)
        self.assertEqual(str(ve.exception), "At least one traveler is required!")

    def test_is_family__True_set_to_False(self):
        t2 = Trip(500, 1, True)

        self.assertEqual(t2.budget, 500.0)
        self.assertEqual(t2.travelers, 1)
        self.assertFalse(t2.is_family)
        self.assertEqual(t2.booked_destinations_paid_amounts, {})

    def test_book_a_trip_happy_case__family_discount(self):
        t = Trip(25000.0, 2, True)

        res = t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 900.0})
        self.assertEqual(t.budget, 24100.0)
        self.assertEqual(res, 'Successfully booked destination Bulgaria! Your budget left is 24100.00')

    def test_book_a_trip_happy_case__no_family_discount(self):
        t = Trip(25000.0, 2, False)

        res = t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 1000.0})
        self.assertEqual(t.budget, 24000.0)
        self.assertEqual(res, 'Successfully booked destination Bulgaria! Your budget left is 24000.00')

    def test_book_a_trip_happy_case__two_bookings(self):
        t = Trip(25000.0, 2, False)

        res = t.book_a_trip('Bulgaria')
        res2 = t.book_a_trip('New Zealand')
        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 1000.0, 'New Zealand': 15000.0})
        self.assertEqual(t.budget, 9000.0)
        self.assertEqual(res, 'Successfully booked destination Bulgaria! Your budget left is 24000.00')
        self.assertEqual(res2, 'Successfully booked destination New Zealand! Your budget left is 9000.00')

    def test_book_a_trip__no_such_destination(self):
        t = Trip(25000.0, 2, False)

        res = t.book_a_trip('Indonesia')
        self.assertEqual(t.booked_destinations_paid_amounts, {})
        self.assertEqual(t.budget, 25000.0)
        self.assertEqual(res, 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip__not_enough_budget_no_discount(self):
        t = Trip(999.99, 2, False)

        res = t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {})
        self.assertEqual(t.budget, 999.99)
        self.assertEqual(res, 'Your budget is not enough!')

    def test_book_a_trip__not_enough_budget_with_discount(self):
        t = Trip(899.99, 2, True)

        res = t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {})
        self.assertEqual(t.budget, 899.99)
        self.assertEqual(res, 'Your budget is not enough!')

    def test_booking_status__no_bookings(self):
        t = Trip(1000, 2, False)
        self.assertEqual(t.booked_destinations_paid_amounts, {})
        res = t.booking_status()
        self.assertEqual(res, """No bookings yet. Budget: 1000.00""")

    def test_booking_status__one_booking(self):
        t = Trip(1000, 1, False)
        t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 500.0})
        res = t.booking_status()
        self.assertEqual(res, """Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 500.00""")

    def test_booking_status__two_bookings(self):
        t = Trip(10000, 1, False)
        t.book_a_trip('New Zealand')
        t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {'New Zealand': 7500.0, 'Bulgaria': 500.0})
        res = t.booking_status()
        self.assertEqual(res, """Booked Destination: Bulgaria
Paid Amount: 500.00
Booked Destination: New Zealand
Paid Amount: 7500.00
Number of Travelers: 1
Budget Left: 2000.00""")

if __name__ == "__main__":
    main()
