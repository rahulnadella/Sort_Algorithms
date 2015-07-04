import mergesort
import unittest

class MergeSortTest(unittest.TestCase):

    def setUp(self):
        self.mergesort = mergesort.MergeSort()

    def tearDown(self):
        self.mergesort = None

    def test_merge_sort(self):
        unsorted_lst = [4, 5, 1, 6, 3]
        test_sort_lst = [1, 3, 4, 5, 6]

        sorted_lst = self.mergesort.merge_sort(unsorted_lst)
        self.assertEqual(sorted_lst, test_sort_lst)

    def test_merge(self):
        left_lst = [1, 2, 6, 7]
        right_lst = [1, 3, 5, 9]
        test_sorted_lst = [1, 1, 2, 3, 5, 6, 7, 9]

        sorted_lst = self.mergesort.merge(left_lst, right_lst)
        self.assertEqual(sorted_lst, test_sorted_lst)

if __name__ == '__main__':
    unittest.main()
