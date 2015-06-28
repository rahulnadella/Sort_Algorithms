class BubbleSort(object):

    def sort_descending(values):
        sorted = True

        while sorted:
            sorted = False
            for element in range(len(values) - 1):
                if values[element] < values[element + 1]:
                    values[element], values[element + 1] = values[element + 1], values[element]
                    sorted = True

    def sort_ascending(values):
        sorted = True

        while sorted:
            sorted = False
            for element in range(0, len(values) - 1):
                if values[element] > values[element + 1]:
                    values[element], values[element + 1] = values[element + 1], values[element]
                    sorted = True
