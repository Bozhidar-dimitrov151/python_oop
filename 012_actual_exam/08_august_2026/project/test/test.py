from project.legendary_item import LegendaryItem
from unittest import TestCase, main


class LegendaryItemTest(TestCase):
    def test_create_valid_item(self):
        self.item = LegendaryItem("Sword-123", 50, 100, 100)

        self.assertEqual(self.item.identifier, "Sword-123")
        self.assertEqual(self.item.power, 50)
        self.assertEqual(self.item.durability, 100)
        self.assertEqual(self.item.price, 100)


    def test_identifier_with_letters_and_digits_and_hyphens(self):
        self.item = LegendaryItem("ABC-123", 50, 100, 100)

        self.assertEqual(self.item.identifier, "ABC-123")

    def test_identifier_too_short(self):
        with self.assertRaises(ValueError) as ve:
            LegendaryItem('ABC', 10, 50, 100)

        self.assertEqual(str(ve.exception), "Identifier must be at least 4 characters long!")

    def test_identifier_contains_invalid_characters(self):
        with self.assertRaises(ValueError) as ve:
            LegendaryItem("ABC_123", 10, 50, 100)

        self.assertEqual(str(ve.exception),"Identifier can only contain letters, digits, or hyphens!")

    def test_identifier_contains_space(self):
        with self.assertRaises(ValueError):
            LegendaryItem("ABC 123", 10, 50, 100)

    #------------------------power-----------------------------------------

    def test_power_zero_is_valid(self):
        item = LegendaryItem("Sword", 0, 50, 100)

        self.assertEqual(item.power, 0)

    def test_power_negative(self):
        with self.assertRaises(ValueError) as context:
            LegendaryItem("Sword", -1, 50, 100)

        self.assertEqual(
            str(context.exception),
            "Power must be a non-negative integer!"
        )

    #--------------------------------durability----------------------------------

    def test_durability_minimum(self):
        item = LegendaryItem("Sword", 10, 1, 100)

        self.assertEqual(item.durability, 1)

    def test_durability_maximum(self):
        item = LegendaryItem("Sword", 10, 100, 100)

        self.assertEqual(item.durability, 100)

    def test_durability_zero(self):
        with self.assertRaises(ValueError) as context:
            LegendaryItem("Sword", 10, 0, 100)

        self.assertEqual(
            str(context.exception),
            "Durability must be between 1 and 100 inclusive!"
        )

    def test_durability_over_100(self):
        with self.assertRaises(ValueError):
            LegendaryItem("Sword", 10, 101, 100)

    #------------------------------------price-------------------------------------------
    def test_price_multiple_of_10(self):
        item = LegendaryItem("Sword", 10, 50, 100)
        self.assertEqual(item.price, 100)

    def test_price_zero(self):
        with self.assertRaises(ValueError) as context:
            LegendaryItem("Sword", 10, 50, 0)

        self.assertEqual(
            str(context.exception),
            "Price must be a multiple of 10 and not 0!"
        )

    def test_price_not_multiple_of_10(self):
        with self.assertRaises(ValueError):
            LegendaryItem("Sword", 10, 50, 15)

    #------------------------------- is_precious -----------------------------------------------

    def test_is_precious_when_power_is_50(self):
        item = LegendaryItem("Sword", 50, 50, 100)

        self.assertTrue(item.is_precious)
    def test_is_precious_when_is_below_50(self):
        item = LegendaryItem("Sword", 49, 50, 100)

        self.assertFalse(item.is_precious)
    #-----------------------------------enhance---------------------------------------------------

    def test_enhance(self):
        item = LegendaryItem("Sword", 20, 50, 100)

        item.enhance()

        self.assertEqual(item.power, 40)
        self.assertEqual(item.price, 110)
        self.assertEqual(item.durability, 60)

    def test_enhance_durability_cannot_exceed_100(self):
        item = LegendaryItem("Sword", 20, 95, 100)

        item.enhance()

        self.assertEqual(item.durability, 100)

    def test_enhance_can_make_item_precious(self):
        item = LegendaryItem("Sword", 30, 50, 100)

        self.assertFalse(item.is_precious)

        item.enhance()

        self.assertTrue(item.is_precious)

    #------------------------------------------evaluate--------------------------
    def test_evaluate_when_item_is_eligible(self):
        item = LegendaryItem("Sword", 50, 80, 100)

        result = item.evaluate(70)

        self.assertEqual(result, "Sword is eligible.")

    def test_evaluate_when_durability_is_too_low(self):
        item = LegendaryItem("Sword", 50, 50, 100)

        result = item.evaluate(60)

        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_when_item_is_not_precious(self):
        item = LegendaryItem("Sword", 49, 80, 100)

        result = item.evaluate(70)

        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_boundary_values(self):
        item = LegendaryItem("Sword", 50, 50, 100)

        result = item.evaluate(50)

        self.assertEqual(result, "Sword is eligible.")

if __name__ == '__main__':
    main()
