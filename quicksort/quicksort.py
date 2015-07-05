"""
Quicksort is a divide and conquer algorithm which relies on a partition
operation: to partition an array an element called a pivot is selected. All
elements smaller than the pivot are moved before it and all greater elements are
moved after it. This can be done efficiently in linear time and in-place. The
lesser and greater sublists are then recursively sorted. This yields average
time complexity of O(n log n), with low overhead, and thus this is a popular algorithm.
Efficient implementations of quicksort (with in-place partitioning) are typically
unstable sorts and somewhat complex, but are among the fastest sorting algorithms
in practice. Together with its modest O(log n) space usage, quicksort is one of
the most popular sorting algorithms and is available in many standard programming
libraries.

The important caveat about quicksort is that its worst-case performance is
O(n^2); while this is rare, in naive implementations (choosing the first or
last element as pivot) this occurs for sorted data, which is a common case. The
most complex issue in quicksort is thus choosing a good pivot element, as
consistently poor choices of pivots can result in drastically slower O(n^2)
performance, but good choice of pivots yields O(n log n) performance, which is
asymptotically optimal. For example, if at each step the median is chosen as the
pivot then the algorithm works in O(n log n). Finding the median, such as by the
median of medians selection algorithm is however an O(n) operation on unsorted
lists and therefore exacts significant overhead with sorting. In practice
choosing a random pivot almost certainly yields O(n log n) performance.

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n^2)
Space Complexity: O(log n)
"""


class QuickSort(object):

  number = 0
  numbers = []

  def sort(values):
    if not values or len(values) == 0:
      return

    QuickSort.numbers = values
    QuickSort.number = len(values)
    QuickSort.__quicksort(0, QuickSort.number - 1)

  @staticmethod
  def __exchange(i, j):
    QuickSort.numbers[i], QuickSort.numbers[
        j] = QuickSort.numbers[j], QuickSort.numbers[i]

  @staticmethod
  def __quicksort(low, high):
    i = int(low)
    j = int(high)
    pivot = QuickSort.numbers[low + int((high - low) / 2)]

    while i <= j:

      while QuickSort.numbers[i] < pivot:
        i += 1

      while QuickSort.numbers[j] > pivot:
        j -= 1

      if i <= j:
        QuickSort.__exchange(i, j)
        i += 1
        j -= 1

    if low < j:
      QuickSort.__quicksort(low, j)

    if i < high:
      QuickSort.__quicksort(i, high)
