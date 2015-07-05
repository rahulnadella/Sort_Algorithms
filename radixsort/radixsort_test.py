import radixsort
import unittest

class RadixSortTest(unittest.TestCase):

    def setUp(self):
        self.radixsort = radixsort.RadixSort

    def tearDown(self):
        self.radixsort = None

    def test_sort(self):
        test_data = [18,5,100,3,1,19,6,0,7,4,2]
        sorted_data = [0,1,2,3,4,5,6,7,18,19,100]

        self.radixsort.sort(test_data)
        self.assertEqual(test_data, sorted_data)

    def test_radixsort(self):
        test_data = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
        self.radixsort.sort(test_data)
        for i in range(1, len(test_data)):
            if test_data[i - 1] > test_data[i]:
                self.fail("radix algorithm sort method fails.")

if __name__ == '__main__':
    unittest.main()
