import unittest
import bubblesort

class Bubblesort(unittest.TestCase):

    def setUp(self):
        self.bubblesort = bubblesort.BubbleSort

    def tearDown(self):
        self.bubblesort = None

    def test_sort_descending(self):
        test_data = [6, 7, 8, 9]
        test_sorted_data = [9, 8, 7, 6]

        self.bubblesort.sort_descending(test_data)
        self.assertEqual(test_data, test_sorted_data)

    def test_sort_ascending(self):
        test_data = [5, 90, 35, 45, 150, 3]
        test_sorted_data = [3, 5, 35, 45, 90, 150]

        self.bubblesort.sort_ascending(test_data)
        self.assertEqual(test_data, test_sorted_data)

    def test_bubble_sort(self):
        test_data = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]

        self.bubblesort.sort_ascending(test_data)
        for i in range(1, len(test_data)):
            if test_data[i - 1] > test_data[i]:
                self.fail("bubblesort sort_ascending method fails")

        self.bubblesort.sort_descending(test_data)
        for i in range(1, len(test_data)):
            if test_data[i - 1] < test_data[i]:
                self.fail("bubblesort sort_descending method fails")

if __name__ == '__main__':
    unittest.main()
