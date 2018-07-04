from heapq import *


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        if len(matrix) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            heappush(heap, (matrix[i][0], i, j))
        for i in range(0, k):
            elem = heappop(heap)
            if i == k - 1:
                return elem[0]
            if elem[2] < m - 1:
                heappush(heap, (matrix[elem[1]][elem[2] + 1], elem[1], elem[2] + 1))

                
