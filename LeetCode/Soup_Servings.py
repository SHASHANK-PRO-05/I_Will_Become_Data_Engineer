class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        N, Q = int(N / 25), N % 25
        N = N + (Q > 0)
        if N > 500:
            return 1
        memo = {}

        def dp(x, y):

            if (x, y) not in memo.keys():
                if x <= 0 or y <= 0:
                    memo[x, y] = 0.5 if x <= 0 and y <= 0 else 1 if x <= 0 else 0
                else:
                    memo[x, y] = 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2, y - 2) + dp(x - 1, y - 3))
            return memo[x, y]

        return dp(N, N)


sol = Solution()
print(sol.soupServings(50))
