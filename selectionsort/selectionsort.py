class SelectionSort(object):

    def sort(values):
      for i in range(len(values)):
        least = i
        for k in range(i + 1, len(values)):
          if values[k] < values[least]:
            least = k

        SelectionSort.swap(values, least, i)

    def swap( A, x, y ):
        A[x], A[y] = A[y], A[x]
