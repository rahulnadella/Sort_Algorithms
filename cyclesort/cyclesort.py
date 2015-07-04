class CycleSort(object):

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
