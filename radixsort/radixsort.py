"""
Radix sort is an algorithm that sorts numbers by processing individual digits.
n numbers consisting of k digits each are sorted in O(n · k) time. Radix sort
can process digits of each number either starting from the least significant
digit (LSD) or starting from the most significant digit (MSD). The LSD algorithm
first sorts the list by the least significant digit while preserving their
relative order using a stable sort. Then it sorts them by the next digit, and so
on from the least significant to the most significant, ending up with a sorted
list. While the LSD radix sort requires the use of a stable sort, the MSD radix
sort algorithm does not (unless stable sorting is desired). In-place MSD radix
sort is not stable. It is common for the counting sort algorithm to be used
internally by the radix sort. A hybrid sorting approach, such as using insertion
sort for small bins improves performance of radix sort significantly.

Worst Case: O(wn)
Worst Space Complexity: O(w + k)
"""


class RadixSort(object):

  """
  Implementation:

  radix sort, like counting sort and bucket sort, is an integer based
  algorithm (i.e. the values of the input array are assumed to be
  integers). Hence radix sort is among the fastest sorting algorithms
  around, in theory. The particular distinction for radix sort is
  that it creates a bucket for each cipher (i.e. digit); as such,
  similar to bucket sort, each bucket in radix sort must be a
  growable list that may admit different keys.

  For decimal values, the number of buckets is 10, as the decimal
  system has 10 numerals/cyphers (i.e. 0,1,2,3,4,5,6,7,8,9). Then
  the keys are continuously sorted by significant digits.
  """
  def sort(lst):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
      max_length = True
      # declare and initialize buckets
      buckets = [list() for _ in range(RADIX)]

      # split lst between lists
      for i in lst:
        tmp = int(i / placement)
        buckets[tmp % RADIX].append(i)
        if max_length and tmp > 0:
          max_length = False

      # empty lists in lst
      a = 0
      for b in range(RADIX):
        buck = buckets[b]
        for i in buck:
          lst[a] = i
          a += 1

      # move to next digit
      placement *= RADIX
