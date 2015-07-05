import cyclesort
import unittest

class CycleSortTest(unittest.TestCase):

    def setUp(self):
        self.cyclesort = cyclesort.CycleSort

    def tearDown(self):
        self.cyclesort = None

    def test_sort(self):
        test_data = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        sorted_lst = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

        self.cyclesort.sort(test_data)
        self.assertEqual(test_data, sorted_lst)

    def test_cyclesort(self):
        test_data = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]

        self.cyclesort.sort(test_data)
        for i in range(1, len(test_data)):
            if test_data[i - 1] > test_data[i]:
              self.fail( "cyclesort sort method fails." )

if __name__ == '__main__':
    unittest.main()
