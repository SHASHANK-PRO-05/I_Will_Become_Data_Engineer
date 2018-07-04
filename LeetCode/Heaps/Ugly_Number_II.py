import heapq


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = heapq.heapify([2, 3, 5])
        visited = {
            2: True,
            3: True,
            5: True
        }
        array = [2, 3, 5]
        for i in range(0, n):
            elem = heapq.heappop(heap)
            for i in range(0, len(array)):
                if elem * array[i] not in visited:
                    visited[elem * array[i]] = True
                    heapq.heappush(elem * array[i])

        return elem
