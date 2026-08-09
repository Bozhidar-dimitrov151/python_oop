from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class SecondHandCarTest(TestCase):
    def test_init(self):
        self.car = SecondHandCar("BMW X5", "SUV", 120000, 25000)

        self.assertEqual(self.car.model, "BMW X5")
        self.assertEqual(self.car.car_type, "SUV")
        self.assertEqual(self.car.mileage, 120000)
        self.assertEqual(self.car.price, 25000)

    def test_below_retail_price_or_equal_raises(self):
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("BMW X5", "SUV", 120000, 1)
        self.assertEqual(str(ve.exception), "Price should be greater than 1.0!")

    def test_mileage_below_or_equal_to_100(self):
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("BMW X5", "SUV", 100, 25000)

        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_success(self):
        car = SecondHandCar("BMW", "SUV", 120000, 20000)
        with self.assertRaises(ValueError) as ve:
            car.set_promotional_price(22000)
        self.assertEqual(str(ve.exception), "You are supposed to decrease the price!")

    def test_need_repair_success(self):
        car = SecondHandCar("Audi", "Sedan", 150000, 10000)

        result = car.need_repair(2000, "New brakes")

        self.assertEqual(
        result,
                "Price has been increased due to repair charges."
            )
        self.assertEqual(car.price, 12000)
        self.assertEqual(car.repairs, ["New brakes"])

    def test_need_repair_impossible(self):
        car = SecondHandCar("Audi", "Sedan", 150000, 10000)

        result = car.need_repair(6000, "New engine")

        self.assertEqual(result, "Repair is impossible!")
        self.assertEqual(car.price, 10000)
        self.assertEqual(car.repairs, [])

    def test_gt_same_type_true(self):
        car1 = SecondHandCar("BMW", "SUV", 120000, 25000)
        car2 = SecondHandCar("Audi", "SUV", 130000, 20000)

        self.assertTrue(car1 > car2)

    def test_gt_same_type_false(self):
        car1 = SecondHandCar("BMW", "SUV", 120000, 18000)
        car2 = SecondHandCar("Audi", "SUV", 130000, 20000)

        self.assertFalse(car1 > car2)

    def test_gt_different_type(self):
        car1 = SecondHandCar("BMW", "SUV", 120000, 25000)
        car2 = SecondHandCar("Audi", "Sedan", 130000, 20000)

        self.assertEqual(
            car1 > car2,
            "Cars cannot be compared. Type mismatch!"
            )


    def test_str(self):
        car = SecondHandCar("BMW X5", "SUV", 120000, 25000)

        expected = (
            "Model BMW X5 | Type SUV | Milage 120000km\n"
            "Current price: 25000.00 | Number of Repairs: 0"
            )

        self.assertEqual(str(car), expected)

    def test_promotional_price_success(self):
        car = SecondHandCar("BMW", "SUV", 120000, 20000)

        result = car.set_promotional_price(18000)

        self.assertEqual(result, "The promotional price has been successfully set.")
        self.assertEqual(car.price, 18000)

if __name__ == "__main__":
    main()
