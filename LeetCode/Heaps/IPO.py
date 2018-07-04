from heapq import *


class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        zipped = zip(Profits, Capital)
        sort = sorted(
            ((-elem[0], elem[1]) for
             elem in zipped))

        i = 0
        heapify(sort)

        temp = 0
        while sort and temp < k:
            ans = []

            while sort and W < sort[0][1]:
                ans.append(heappop(sort))
            if not sort:
                return W

            W = W - sort[0][0]

            heappop(sort)
            for elem in ans:
                heappush(sort, elem)
            temp += 1
        return W


sol = Solution()
print(sol.findMaximizedCapital(11,
                               11,
                               [1, 2, 3],
                               [11, 12, 13]))
