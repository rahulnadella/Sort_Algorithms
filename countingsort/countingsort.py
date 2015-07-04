class CountingSort(object):

    def sort(array):
        maximum = max(array)
        minimum = min(array)
        count_array = [0]*(maximum-minimum+1)

        for val in array:
            count_array[val-minimum] += 1

        sorted_array = []
        for i in range(minimum, maximum+1):
            if count_array[i-minimum] > 0:
                for j in range(0, count_array[i-minimum]):
                    sorted_array.append(i)

        return sorted_array
