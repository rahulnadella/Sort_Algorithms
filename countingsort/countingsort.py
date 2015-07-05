"""
Counting sort is applicable when each input is known to belong to a particular
set, S, of possibilities. The algorithm runs in O(|S| + n) time and O(|S|)
memory where n is the length of the input. It works by creating an integer array
of size |S| and using the ith bin to count the occurrences of the ith member of
S in the input. Each input is then counted by incrementing the value of its
corresponding bin. Afterward, the counting array is looped through to arrange all
of the inputs in order. This sorting algorithm often cannot be used because S
needs to be reasonably small for the algorithm to be efficient, but it is extremely
fast and demonstrates great asymptotic behavior as n increases. It also can be
modified to provide stable behavior.

Best Case: O(n + k)
Average Case: O(n + k)
Worst Case: O(n + k)
Space Complexity: O(n + k)
"""


class CountingSort(object):

  def sort(array):
    maximum = max(array)
    minimum = min(array)
    count_array = [0] * (maximum - minimum + 1)

    for val in array:
      count_array[val - minimum] += 1

    sorted_array = []
    for i in range(minimum, maximum + 1):
      if count_array[i - minimum] > 0:
        for j in range(0, count_array[i - minimum]):
          sorted_array.append(i)

    return sorted_array
