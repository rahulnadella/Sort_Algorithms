class InsertionSort(object):

    def sort(lst):

        for i in range(1, len(lst)):
            value_to_insert = lst[i]
            index = i
            while index > 0 and value_to_insert < lst[index - 1]:
                lst[index] = lst[index - 1]
                index -= 1
            lst[index] = value_to_insert
