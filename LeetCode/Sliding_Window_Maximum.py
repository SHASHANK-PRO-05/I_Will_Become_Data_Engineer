import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        array = []
        heap = []
        for i in range(0, k):
            heapq.heappush(heap, (-nums[i], i))

        for i in range(k, len(nums)):

            while heap[0][1] < i - k:
                heapq.heappop(heap)

            elem = heap[0]
            array.append(-elem[0])
            heapq.heappush(heap, (-nums[i], i))
        i = i + 1
        while heap[0][1] < i - k:
            heapq.heappop(heap)

        elem = heap[0]
        array.append(-elem[0])
        return array


sol = Solution()
print(sol.maxSlidingWindow([1, -1], 1))
