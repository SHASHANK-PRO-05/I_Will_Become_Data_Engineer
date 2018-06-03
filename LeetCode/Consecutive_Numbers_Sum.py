class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        while N & 1 == 0:
            N = N >> 1

        ans = 1
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                e = e + 1
                N = N / d
            ans *= e + 1
            d = d + 2

        if N > 1: ans *= 2
        return ans


sol = Solution()
print(sol.consecutiveNumbersSum(15))
