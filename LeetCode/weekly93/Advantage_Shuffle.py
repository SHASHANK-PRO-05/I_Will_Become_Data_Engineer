from heapq import *


class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = [-1] * len(A)
        uselessA = []
        heapify(A)
        heap = [(B[i], i) for i in range(len(B))]
        heapify(heap)
        while A:
            elem = heappop(A)
            if heap[0][0] < elem:
                b_poped = heappop(heap)
                ans[b_poped[1]] = elem
            else:
                uselessA.append(elem)
        for i in range(len(B)):
            if ans[i] == -1:
                ans[i] = uselessA.pop()
        return ans


sol = Solution()
print(sol.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
