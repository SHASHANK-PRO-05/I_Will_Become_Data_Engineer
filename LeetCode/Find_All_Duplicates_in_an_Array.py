class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ansList = []
        for i in range(0, len(nums)):
            val = abs(nums[i]) - 1
            nums[val] = nums[val] * -1
            if nums[val] > 0:
                ansList.append(val + 1)
        return ansList
