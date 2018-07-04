import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        firstHalf, secondHalf = self.heaps
        heapq.heappush(secondHalf, num)
        heapq.heappush(firstHalf, -heapq.heappop(secondHalf))
        if len(secondHalf) < len(firstHalf):
            heapq.heappush(secondHalf, -heapq.heappop(firstHalf))

    def findMedian(self):
        """
        :rtype: float
        """
        firstHalf, secondHalf = self.heaps
        if len(secondHalf) > len(firstHalf):
            return float(secondHalf[0])
        else:
            return (secondHalf[0] - firstHalf[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
