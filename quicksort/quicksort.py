class QuickSort(object):

    number = 0
    numbers = []

    def sort(values):
        if not values or len(values) == 0:
            return;

        QuickSort.numbers = values
        QuickSort.number = len(values)
        QuickSort.__quicksort(0, QuickSort.number - 1)

    def __exchange(i, j):
        QuickSort.numbers[i], QuickSort.numbers[j] = QuickSort.numbers[j], QuickSort.numbers[i]

    def __quicksort(low, high):
        i = int(low)
        j = int(high)
        pivot = QuickSort.numbers[low + int((high - low)/2)]

        while i <= j:

            while QuickSort.numbers[i] < pivot:
                i += 1

            while QuickSort.numbers[j] > pivot:
                j -= 1

            if i <= j:
                QuickSort.__exchange(i, j)
                i += 1
                j -= 1

        if low < j:
            QuickSort.__quicksort(low, j)

        if i < high:
            QuickSort.__quicksort(i, high)
