import collections


class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter()
        for i, row in enumerate(A):
            for j, a in enumerate(row):
                if a:
                    for i1, row1 in enumerate(B):
                        for j1, b in enumerate(row1):
                            if b:
                                counter[i - i1, j - j1] += 1

        return max(counter.values() or [0])
