class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res = 0
        numInAge, sumInAge = [0] * 121, [0] * 121
        for i, age in enumerate(ages):
            numInAge[age] += 1
        for i in range(1, 121):
            sumInAge[i] = numInAge[i] + sumInAge[i - 1]

        for i in range(15, 121):
            if numInAge[i] == 0: continue
            count = sumInAge[i] - sumInAge[int(i / 2 + 7)]

            res += count * numInAge[i] - numInAge[i]

        return res


sol = Solution()
print(sol.numFriendRequests([20, 30, 100, 110, 120]))
