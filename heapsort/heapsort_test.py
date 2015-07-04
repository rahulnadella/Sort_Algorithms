import heapsort
import unittest

class HeapSortTest(unittest.TestCase):

    def setUp(self):
        self.heapsort = heapsort.HeapSort

    def tearDown(self):
        self.heapsort = None

    def test_sort(self):
        test_data = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        test_sorted_lst = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

        self.heapsort.sort(test_data)
        self.assertEqual(test_data, test_sorted_lst)

        test_data = [32, 46, 77, 4344564, 7322, 3, 46, 7, 32457, 7542, 4, 667, 54]
        test_sorted_lst = [3, 4, 7, 32, 46, 46, 54, 77, 667, 7322, 7542, 32457, 4344564]

        self.heapsort.sort(test_data)
        self.assertEqual(test_data, test_sorted_lst)

if __name__ == '__main__':
    unittest.main()
