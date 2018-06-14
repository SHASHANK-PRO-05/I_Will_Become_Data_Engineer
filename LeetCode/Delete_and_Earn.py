class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        array = sorted(map.items())
        ans = array[0][0] * array[0][1]
        prevMax = [0] * len(array)
        curMax = [0] * len(array)
        curMax[0] = ans
        for i in range(1, len(array)):
            prevMax[i] = ans

            if array[i][0] == array[i - 1][0] + 1:
                curMax[i] = prevMax[i - 1] + array[i][0] * array[i][1]
            else:
                curMax[i] = ans + array[i][0] * array[i][1]
            ans = max(ans, curMax[i])
        # print(array)
        # print(prevMax)
        # print(curMax)
        return ans

