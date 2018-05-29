class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """

        dp = [0.0] * (N + W + 1)
        for k in range(K, N + 1):
            dp[k] = 1.0
        S = min(N - K + 1, W)
        for k in range(K - 1, -1, -1):
            dp[k] = S / float(W)
            S = S + dp[k] - dp[k + W]
        return round(dp[0], 5)


sol = Solution()
print(sol.new21Game(1, 1, 1))
