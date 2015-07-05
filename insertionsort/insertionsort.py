"""
Insertion sort is a simple sorting algorithm that is relatively efficient for
small lists and mostly sorted lists, and is often used as part of more
sophisticated algorithms. It works by taking elements from the list one by one
and inserting them in their correct position into a new sorted list. In arrays,
the new list and the remaining elements can share the array's space, but
insertion is expensive, requiring shifting all following elements over by one.
Shell sort is a variant of insertion sort that is more efficient for larger lists.

Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
"""


class InsertionSort(object):

  """
  Implementation:

  Insertion sort is good for collections that are very small
  or nearly sorted. Otherwise it's not a good sorting algorithm:
  it moves data around too much. Each time an insertion is made,
  all elements in a greater position are shifted.
  """
  def sort(lst):

    for i in range(1, len(lst)):
      value_to_insert = lst[i]
      index = i
      while index > 0 and value_to_insert < lst[index - 1]:
        lst[index] = lst[index - 1]
        index -= 1
      lst[index] = value_to_insert
