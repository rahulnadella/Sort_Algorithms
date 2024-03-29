import unittest
import selectionsort

class SelectionSortTest(unittest.TestCase):

    def setUp(self):
        self.selectionsort = selectionsort.SelectionSort

    def tearDown(self):
        self.selectionsort = None

    def test_sort(self):
        test_data = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
        test_sorted_data = [0, 1, 2, 3, 4, 5, 6, 7, 18, 19, 100]

        self.selectionsort.sort(test_data)
        self.assertEqual(test_data, test_sorted_data)

    def testSelectionsort( self ):
        test_data = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
        self.selectionsort.sort(test_data)
        for i in range(1, len(test_data)):
            if test_data[i - 1] > test_data[i]:
                self.fail("selectionsort method fails.")

if __name__ == '__main__':
    unittest.main()
