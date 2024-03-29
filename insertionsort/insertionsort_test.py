import insertionsort
import unittest

class InsertionSortTest(unittest.TestCase):

    def setUp(self):
        self.insertionsort = insertionsort.InsertionSort

    def tearDown(self):
        self.insertionsort = None

    def test_sort(self):
        test_data = [45, 67, 2, 3, 5, 7, 898, 9, 6, 5, 4, 33, 3, 35566, 1]
        sorted_lst = [1, 2, 3, 3, 4, 5, 5, 6, 7, 9, 33, 45, 67, 898, 35566]

        self.insertionsort.sort(test_data)
        self.assertEqual(test_data, sorted_lst)

    def testInsertionsort(self):
        test_data = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        self.insertionsort.sort(test_data)
        for i in range(1, len(test_data)):
            if test_data[i - 1] > test_data[i]:
                self.fail("insertionsort method fails.")

if __name__ == '__main__':
    unittest.main()
