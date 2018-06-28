import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        zipped = zip(quality, wage)
        array = sorted([(w / q, q, w) for q, w in zipped])
        ans = float('inf')
        heap = []
        sum = 0
        for i in range(0, len(array)):
            heapq.heappush(heap, -1 * array[i][1])
            sum += array[i][1]

            if len(heap) > K:
                sum = sum + heapq.heappop(heap)

            if len(heap) == K:
                ans = min(ans, array[i][0] * sum)
        return ans


sol = Solution()
print(sol.mincostToHireWorkers([10, 20, 5],
                               [70, 50, 30],
                               2))
