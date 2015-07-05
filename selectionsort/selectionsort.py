"""
Selection sort is an in-place comparison sort. It has O(n^2) complexity, making
it inefficient on large lists, and generally performs worse than the similar
insertion sort. Selection sort is noted for its simplicity, and also has
performance advantages over more complicated algorithms in certain situations.

The algorithm finds the minimum value, swaps it with the value in the first
position, and repeats these steps for the remainder of the list. It does no more
than n swaps, and thus is useful where swapping is very expensive.

Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
"""


class SelectionSort(object):

  def sort(values):
    for i in range(len(values)):
      least = i
      for k in range(i + 1, len(values)):
        if values[k] < values[least]:
          least = k

      SelectionSort.__swap(values, least, i)

  @staticmethod
  def __swap(A, x, y):
    A[x], A[y] = A[y], A[x]
