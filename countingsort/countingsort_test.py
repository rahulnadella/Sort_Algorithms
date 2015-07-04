import countingsort
import unittest

class CountingSortTest(unittest.TestCase):

    def setUp(self):
        self.countingsort = countingsort.CountingSort

    def tearDown(self):
        self.countingsort = None

    def test_sort(self):
        test_data = [3, 2, -1, 1, 5, 0, 10, 18, 25, 25]
        sorted_lst = [-1, 0, 1, 2, 3, 5, 10, 18, 25, 25]

        count_lst = self.countingsort.sort(test_data)
        self.assertEqual(count_lst, sorted_lst)

if __name__ == '__main__':
    unittest.main()
