import operator

"""
Merge sort takes advantage of the ease of merging already sorted lists into a
new sorted list. It starts by comparing every two elements (i.e., 1 with 2, then
3 with 4...) and swapping them if the first should come after the second. It then
merges each of the resulting lists of two into lists of four, then merges those
lists of four, and so on; until at last two lists are merged into the final
sorted list. Of the algorithms described here, this is the first that scales
well to very large lists, because its worst-case running time is O(n log n).
It is also easily applied to lists, not only arrays, as it only requires
sequential access, not random access. However, it has additional O(n) space
complexity, and involves a large number of copies in simple implementations.

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
Space Complexity: O(n)
"""


class MergeSort(object):

  def merge_sort(self, lst):

    if len(lst) <= 1:
      return lst
    mid = len(lst) // 2
    left = self.merge_sort(lst[:mid])
    right = self.merge_sort(lst[mid:])
    return self.merge(left, right)

  def merge(self, l, r):

    result = []
    while l and r:
      if l[-1] > r[-1]:
        result.append(l.pop())
      else:
        result.append(r.pop())
    result += (l + r)[::-1]
    result.reverse()
    return result
