import operator

class MergeSort(object):

    def merge_sort(self, lst):

        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, l, r):

        result = []
        while l and r:
            if l[-1] > r[-1]:
                result.append(l.pop())
            else:
                result.append(r.pop())
        result+=(l+r)[::-1]
        result.reverse()
        return result
