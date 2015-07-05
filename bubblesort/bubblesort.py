"""
Bubble sort is a simple sorting algorithm. The algorithm starts at the beginning
of the data set. It compares the first two elements, and if the first is greater
than the second, it swaps them. It continues doing this for each pair of adjacent
elements to the end of the data set. It then starts again with the first two
elements, repeating until no swaps have occurred on the last pass. This algorithm's
average and worst-case performance is O(n^2), so it is rarely used to sort large,
unordered data sets. Bubble sort can be used to sort a small number of items (where
its asymptotic inefficiency is not a high penalty). Bubble sort can also be used
efficiently on a list of any length that is nearly sorted (that is, the elements
are not significantly out of place). For example, if any number of elements are
out of place by only one position (e.g. 0123546789 and 1032547698), bubble sort's
exchange will get them in order on the first pass, the second pass will find all
elements in order, so the sort will take only 2n time.

Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
"""


class BubbleSort(object):

  def sort_descending(values):
    sorted = True

    while sorted:
      sorted = False
      for element in range(len(values) - 1):
        if values[element] < values[element + 1]:
          values[element], values[
              element + 1] = values[element + 1], values[element]
          sorted = True

  def sort_ascending(values):
    sorted = True

    while sorted:
      sorted = False
      for element in range(0, len(values) - 1):
        if values[element] > values[element + 1]:
          values[element], values[
              element + 1] = values[element + 1], values[element]
          sorted = True
