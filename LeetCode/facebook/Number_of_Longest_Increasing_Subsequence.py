class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        m = [0 for i in range(len(nums))]
        count = [0 for i in range(len(nums))]
        maxSoFar = 0
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            m[i] = 1
            count[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maxTemp = m[j] + 1
                    if maxTemp == m[i]:
                        count[i] += count[j]
                    elif maxTemp > m[i]:
                        m[i] = maxTemp
                        count[i] = count[j]
            if m[i] > maxSoFar:
                maxSoFar = m[i]
                ans = count[i]
            elif m[i] == maxSoFar:
                ans += count[i]
        return ans


sol = Solution()
print(sol.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
