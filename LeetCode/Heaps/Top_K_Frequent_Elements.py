from heapq import *


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for elem in nums:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1

        heap = []
        for key, elem in d.items():
            heappush(heap, (-elem, key))
        ans = [0] * k
        for i in range(0, k):
            ans[i] = heappop(heap)[1]
        return ans


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3],
                       2))
