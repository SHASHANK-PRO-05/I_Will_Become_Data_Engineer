from heapq import *
import random
import math


class HeapSimulation:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        heap = []

        for i in range(0, len(nums) - 1):
            heappush(heap, (nums[i + 1] - nums[i], i, i + 1))

        for i in range(1, k + 1):
            elem = heappop(heap)
            if i == k:
                return elem[0]
            if elem[2] + 1 < len(nums):
                heappush(heap, (nums[elem[2] + 1] - nums[elem[1]], elem[1], elem[2] + 1))

        return None


def simulation():
    n = 10000
    array = [0] * n
    seed = 1000000
    for i in range(0, n):
        array[i] = random.randint(0, seed + 1)

    k = random.randint(1, (n * (n - 1)) / 2)
    print(array)
    print(k)
    # sol = Solution()
    # print(sol.smallestDistancePair(array, k))
    # sol = HeapSimulation()
    # print(sol.smallestDistancePair(array, k))
    sol = Solution()
    print(sol.smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8],
                                   18))


class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums)

        self.nums = nums
        MIN = nums[0]
        MAX = nums[len(nums) - 1]
        start = 0
        end = MAX - MIN
        ans = -1

        while start <= end:

            mid = int(math.ceil((start + end) / 2))
            temp = self.calculateForEveryElement(mid)

            if temp < k:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        return ans

    def calculateForEveryElement(self, dist):
        ans = 0
        for i in range(0, len(self.nums)):
            ans += self.binarySearchFunc(i, dist) - i
        return ans

    def binarySearchFunc(self, i, dist):
        start = i
        end = len(self.nums) - 1
        ans = i
        while start <= end:
            mid = int((start + end) / 2)
            if self.nums[mid] - self.nums[i] <= dist:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


if __name__ == "__main__":
    simulation()
