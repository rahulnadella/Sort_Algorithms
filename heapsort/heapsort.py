"""
Heapsort is a much more efficient version of selection sort. It also works by
determining the largest (or smallest) element of the list, placing that at the
end (or beginning) of the list, then continuing with the rest of the list, but
accomplishes this task efficiently by using a data structure called a heap, a
special type of binary tree. Once the data list has been made into a heap, the
root node is guaranteed to be the largest (or smallest) element. When it is
removed and placed at the end of the list, the heap is rearranged so the largest
element remaining moves to the root. Using the heap, finding the next largest
element takes O(log n) time, instead of O(n) for a linear scan as in simple
selection sort. This allows Heapsort to run in O(n log n) time, and this is
also the worst case complexity.

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
Space Complexity: O(1)
"""


class HeapSort(object):

  def sort(a):

    HeapSort.__heapify(a, len(a))
    end = len(a) - 1
    while end > 0:
      a[end], a[0] = a[0], a[end]
      end -= 1
      HeapSort.__sift_down(a, 0, end)

  @staticmethod
  def __heapify(a, count):

    start = int((count - 2) / 2)
    while start >= 0:
      HeapSort.__sift_down(a, start, count - 1)
      start -= 1

  @staticmethod
  def __sift_down(a, start, end):

    root = start
    while (root * 2 + 1) <= end:
      child = root * 2 + 1
      swap = root
      if a[swap] < a[child]:
        swap = child
      if (child + 1) <= end and a[swap] < a[child + 1]:
        swap = child + 1
      if swap != root:
        a[root], a[swap] = a[swap], a[root]
        root = swap
      else:
        return
