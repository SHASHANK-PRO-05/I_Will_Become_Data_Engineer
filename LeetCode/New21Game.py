class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        res = [0.0] * (N + W + 1)
        S = 0
        for i in range(K, N + 1):
            S += 1
            res[i] = 1

        for i in range(K - 1, -1, -1):
            res[i] = float(S) / float(W)
            S = S + res[i] - res[i + W]

        return round(res[0], 5)


sol = Solution()
print(sol.new21Game(21, 17, 10))
