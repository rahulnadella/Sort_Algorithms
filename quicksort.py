class QuickSort(object):

    numbers = []
    number = 0

    def exchange(self, i, j):
        temp = QuickSort.numbers[i]
        QuickSort.numbers[i] = QuickSort.numbers[j]
        QuickSort.numbers[j] = temp

    def quicksort(self, low, high):
        i = int(low)
        j = int(high)
        pivot = QuickSort.numbers[low + int((high - low)/2)]

        while i <= j:

            while QuickSort.numbers[i] < pivot:
                i += 1

            while QuickSort.numbers[j] > pivot:
                j -= 1


            if i <= j:
                QuickSort().exchange(i, j)
                i += 1
                j -= 1


        if low < j:
            QuickSort().quicksort(low, j)

        if i < high:
            QuickSort().quicksort(i, high)

    def sort(self, values):
        if not values or len(values) == 0:
            return;

        QuickSort.numbers = values
        QuickSort.number = len(values)
        QuickSort().quicksort(0, QuickSort.number - 1)

QuickSort().sort([5, 3])
