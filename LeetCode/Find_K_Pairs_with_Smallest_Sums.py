from heapq import *


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m == 0:
            return []
        array = [(nums1[0] + nums2[0], 0, 0)]
        output = []
        s = set([(0, 0)])
        while len(output) < k and array:
            elem = heappop(array)
            print(elem)
            output.append([nums1[elem[1]], nums2[elem[2]]])
            if elem[1] + 1 < len(nums1) and (elem[1] + 1, elem[2]) not in s:
                heappush(array, (nums1[elem[1] + 1] + nums2[elem[2]], elem[1] + 1, elem[2]))
                s.add((elem[1] + 1, elem[2]))
            if elem[2] + 1 < len(nums2) and (elem[1], elem[2] + 1) not in s:
                heappush(array, (nums1[elem[1]] + nums2[elem[2] + 1], elem[1], elem[2] + 1))
                s.add((elem[1], elem[2] + 1))
        return output


sol = Solution()
print(sol.kSmallestPairs([1, 1, 2],
                         [1, 2, 3],
                         10))
