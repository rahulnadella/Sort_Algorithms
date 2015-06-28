class SelectionSort(object):

    def sort( aList ):
      for i in range(len(aList)):
        least = i
        for k in range(i + 1 , len(aList)):
          if aList[k] < aList[least]:
            least = k

        SelectionSort.swap( aList, least, i )

    def swap( A, x, y ):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp
