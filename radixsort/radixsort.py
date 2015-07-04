class RadixSort(object):

    def sort(lst):
        RADIX = 10
        max_length = False
        tmp, placement = -1, 1

        while not max_length:
            max_length = True
            # declare and initialize buckets
            buckets = [list() for _ in range(RADIX)]

            # split lst between lists
            for i in lst:
                tmp = int(i / placement)
                buckets[tmp % RADIX].append(i)
                if max_length and tmp > 0:
                    max_length = False

            # empty lists in lst
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    lst[a] = i
                    a += 1

            # move to next digit
            placement *= RADIX
