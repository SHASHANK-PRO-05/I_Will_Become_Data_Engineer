from heapq import *


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        for i in range(0, len(s)):
            if s[i] in map:
                map[s[i]] -= 1
            else:
                map[s[i]] = -1

        heap = []
        for key, item in map.items():
            heappush(heap, (item, key))

        ans = ''
        while len(heap) != 0:
            elem = heappop(heap)
            for i in range(0, -elem[0]):
                ans += elem[1]

        return ans


sol = Solution()
print(sol.frequencySort("cccaaa"))
