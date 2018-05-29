class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            if start == end:
                return nums[start]
            mid = int((start + end) / 2)
            if nums[mid] == nums[mid + 1]:
                if mid + 1 == end:
                    return nums[mid - 1]
                end = mid + 1
            elif nums[mid] == nums[mid - 1]:
                start = mid + 1
            else:
                return nums[mid]


sol = Solution()
print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
