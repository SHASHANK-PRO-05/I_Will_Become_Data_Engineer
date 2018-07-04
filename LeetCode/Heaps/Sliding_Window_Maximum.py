import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        array = [-1] * (len(nums) - k + 1)
        heap = []

        for i in range(0, k):
            heapq.heappush(heap, (-nums[i], i))
        array[0] = -heap[0][0]
        index = 1
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            elem = heap[0]
            while elem[1] < i - k:
                heapq.heappop(heap)
                elem = heap[0]
            array[index] = -elem[0]
            index += 1
        return array
