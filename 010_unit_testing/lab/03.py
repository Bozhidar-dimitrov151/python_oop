class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase, main

class ListTest(TestCase):
    def setUp(self):
        self.n_list = IntegerList(1,2,3,4,5,6,7,8,9)

    def test_init(self):
        n_list = IntegerList(1,2,3,4,5,6,7)
        self.assertEqual([1,2,3,4,5,6,7], n_list.get_data())

    def test_add_arg_not_an_int(self):
        with self.assertRaises(ValueError) as ve:
            self.n_list.add(4.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_arg(self):
        expected_result = [1,2,3,4,5,6,7,8,9,10]

        self.n_list.add(10)

        self.assertEqual(expected_result, self.n_list.get_data())

    def test_remove_correct_idx(self):
        expected_result = [1, 2, 3, 4, 6, 7, 8, 9]

        self.n_list.remove_index(4)

        self.assertEqual(expected_result, self.n_list.get_data())

    def test_get_incorrect_idx(self):
        with self.assertRaises(IndexError) as ie:
            self.n_list.get(15)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_insert_incorrect_idx(self):
        with self.assertRaises(IndexError) as ie:
            self.n_list.insert(15, 1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct_idx(self):
        expected_res = 1

        self.assertEqual(expected_res, self.n_list.get_data()[0])

    def test_insert_correct_idx(self):
        expected_result = [1, 1000, 2, 3, 4, 5, 6, 7, 8, 9]

        self.n_list.insert(1, 1000)

        self.assertEqual(expected_result, self.n_list.get_data())

    def test_get_biggest_element(self):
        expected_result = 9

        self.assertEqual(expected_result, self.n_list.get_biggest())

    def test_get_index(self):
        result = self.n_list.get_index(1)

        self.assertEqual(0, result)
if __name__ == '__main__':
    main()