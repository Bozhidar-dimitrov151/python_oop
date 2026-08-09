from project_1.gallery import Gallery

import unittest


class TestGallery(unittest.TestCase):

    def setUp(self):
        self.gallery = Gallery("ArtSpace", "NewYork", 250.0)

    def test_gallery_name_valid(self):
        self.gallery.gallery_name = "NewGallery"
        self.assertEqual(self.gallery.gallery_name, "NewGallery")

        self.gallery.gallery_name = "NewGallery33"
        self.assertEqual(self.gallery.gallery_name, "NewGallery33")

    def test_gallery_name_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.gallery.gallery_name = " "
        self.assertEqual(str(context.exception), "Gallery name can contain letters and digits only!")

        with self.assertRaises(ValueError) as context:
            self.gallery.gallery_name = "New-Gallery20"
        self.assertEqual(str(context.exception), "Gallery name can contain letters and digits only!")

    def test_city_valid(self):
        self.gallery.city = "Boston"
        self.assertEqual(self.gallery.city, "Boston")

        self.gallery.city = "london"
        self.assertEqual(self.gallery.city, "london")

        self.gallery.city = "LA3"
        self.assertEqual(self.gallery.city, "LA3")

    def test_city_invalid_start(self):
        with self.assertRaises(ValueError) as context:
            self.gallery.city = "1Boston"
        self.assertEqual(str(context.exception), "City name must start with a letter!")

        with self.assertRaises(ValueError) as context:
            self.gallery.city = "%Boston"
        self.assertEqual(str(context.exception), "City name must start with a letter!")

        with self.assertRaises(ValueError) as context:
            self.gallery.city = ""
        self.assertEqual(str(context.exception), "City name must start with a letter!")

    def test_area_sq_m_valid(self):
        self.gallery.area_sq_m = 0.001
        self.assertEqual(self.gallery.area_sq_m, 0.001)

        self.gallery.area_sq_m = 300.0
        self.assertEqual(self.gallery.area_sq_m, 300.0)

    def test_area_sq_m_invalid_negative(self):
        with self.assertRaises(ValueError) as context:
            self.gallery.area_sq_m = -2000.0
        self.assertEqual(str(context.exception), "Gallery area must be a positive number!")

        with self.assertRaises(ValueError) as context:
            self.gallery.area_sq_m = -0.001
        self.assertEqual(str(context.exception), "Gallery area must be a positive number!")

    def test_area_sq_m_invalid_zero(self):
        with self.assertRaises(ValueError) as context:
            self.gallery.area_sq_m = 0.0
        self.assertEqual(str(context.exception), "Gallery area must be a positive number!")

    def test_add_exhibition_success(self):
        result = self.gallery.add_exhibition("Impressionism", 2023)
        self.assertEqual(result, 'Exhibition "Impressionism" added for the year 2023.')
        self.assertIn("Impressionism", self.gallery.exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_add_exhibition_duplicate(self):
        self.gallery.add_exhibition("Impressionism", 2023)
        result = self.gallery.add_exhibition("Impressionism", 2023)
        self.assertEqual(result, 'Exhibition "Impressionism" already exists.')
        self.assertEqual(len(self.gallery.exhibitions), 1)

        self.gallery.add_exhibition("Impressionism", 2023)
        result = self.gallery.add_exhibition("Impressionism", 2024)
        self.assertEqual(result, 'Exhibition "Impressionism" already exists.')
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_remove_exhibition_success(self):
        self.gallery.add_exhibition("Impressionism", 2024)
        self.assertEqual(len(self.gallery.exhibitions), 1)

        result = self.gallery.remove_exhibition("Impressionism")
        self.assertEqual(result, 'Exhibition "Impressionism" removed.')
        self.assertNotIn("Impressionism", self.gallery.exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), 0)

    def test_remove_exhibition_not_found(self):
        self.gallery.add_exhibition("Impressionism", 2024)
        self.assertEqual(len(self.gallery.exhibitions), 1)

        result = self.gallery.remove_exhibition("NonExistentExhibition")
        self.assertEqual(result, 'Exhibition "NonExistentExhibition" not found.')
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_list_exhibitions_open(self):
        self.gallery.add_exhibition("Impressionism", 2024)
        self.gallery.open_to_public = True
        exhibitions = self.gallery.list_exhibitions()
        self.assertIn("Impressionism: 2024", exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_list_exhibitions_open__multiple(self):
        self.gallery.add_exhibition("Impressionism", 2023)
        self.gallery.add_exhibition("Romanticism", 2024)
        self.gallery.open_to_public = True
        exhibitions = self.gallery.list_exhibitions()
        self.assertIn("Impressionism: 2023", exhibitions)
        self.assertIn("Romanticism: 2024", exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), 2)

    def test_list_exhibitions_closed(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, 'Gallery ArtSpace is currently closed for public! Check for updates later on.')

    def test_list_exhibitions_closed__with_data(self):
        self.gallery.add_exhibition("Impressionism", 2023)
        self.gallery.add_exhibition("Romanticism", 2024)
        self.assertEqual(len(self.gallery.exhibitions), 2)
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, 'Gallery ArtSpace is currently closed for public! Check for updates later on.')


if __name__ == '__main__':
    unittest.main()
