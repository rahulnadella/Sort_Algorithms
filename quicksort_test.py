import unittest
import quicksort

class QuickSortTest(unittest.TestCase):

    def setUp(self):
        self.quicksort = quicksort.QuickSort()

    def tearDown(self):
        self.quicksort = None

    def test_null(self):
        self.assertIsNone(self.quicksort.sort(None))

    def test_empty(self):
        values = []
        self.assertIsNone(self.quicksort.sort(values))

    def test_simple_element(self):
        test = [5, 4]
        self.quicksort.sort(test)
        self.assertEqual(test, [4, 5])

    def test_sort(self):
        test_array = [4, 3, 9, 2, 10, 22, 1, 5]
        sorted_array = [1, 2, 3, 4, 5, 9, 10, 22]

        self.quicksort.sort(test_array)
        self.assertEqual(test_array, sorted_array)

if __name__ == '__main__':
    unittest.main()
