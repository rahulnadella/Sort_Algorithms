"""
Given a sequence of objects, such as an array of integers; if the
elements are not arranged in order that is because some of them
have switched places among themselves. For example, [4,1,2,3,5,0]
is not in order because 4,5,0 have traded places (1 bad group).
[4,2,3,7,5,0,1] is not in order because 4,5,0 have traded places
and 2,3,7,1 have traded places (two bad groups). In discrete
mathematics, each group, bad or good, is known as a cycle or an
orbit.

The basis for cyclesort is that if the elements of each bad group
were to return to their correct positions, then the entire
sequence would be sorted.

CycleSort has great merit because it improves the life expectancy
of computer memories. During cyclesort, each element is moved once
at maximum. Recall that each time the data in a block of memory is
changed, the memory degrades.

Best Case: O(n^2)
Average Case: O(n^2)
Worst Case:  O(n^2)
Space Complexity: O(n)
"""


class CycleSort(object):

  """
  Given a disordered list of integers (or any other items),
  rearrange the integers in natural order.
  """
  def sort(lst):
    writes = 0

    for cs in range(len(lst) - 1):
      # assume the element at lst[cs] is out of place
      seeker = lst[cs]
      pos = cs
      # find the correct position (pos) of seeker
      for i in range(cs + 1, len(lst)):
        if lst[i] < seeker:
          pos += 1

      # if seeker is already in correct position, move on
      if pos == cs:
        continue

      # move index pos after duplicates if any
      while seeker == lst[pos]:
        pos += 1

      # Make a switch: seeker gets index pos, its rightful
      # home; whatever element was at pos is now the seeker
      # in search of a rightful home.

      seeker = CycleSort.set_value(lst, seeker, pos)
      # track the number of writes
      writes += 1

      #  complete the current cycle before moving to the next
      #  cycle. At the end of the current cycle, pos will
      #  equal cs; which should make sense since a cycle
      #  always ends where it began.

      while pos != cs:
        # same as block of code above
        pos = cs
        for i in range(cs + 1, len(lst)):
          if lst[i] < seeker:
            pos += 1

        while seeker == lst[pos]:
          pos += 1

        seeker = CycleSort.set_value(lst, seeker, pos)
        writes += 1

      return writes

  @staticmethod
  def set_value(lst, data, index):
    try:
      return lst[index]
    finally:
      lst[index] = data
