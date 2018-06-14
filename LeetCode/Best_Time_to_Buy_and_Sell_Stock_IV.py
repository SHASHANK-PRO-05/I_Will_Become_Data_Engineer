class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = []
        for i in range(0, k + 1):
            dp.append([0] * len(prices))

        for i in range(1, k + 1):
            tempMax = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], tempMax + prices[j])
                tempMax = max(tempMax, dp[i - 1][j - 1] - prices[j])

        return max(dp[k])
