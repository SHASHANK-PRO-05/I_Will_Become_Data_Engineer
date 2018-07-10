# class Solution:
#     def findPaths(self, m, n, N, i, j):
#         """
#         :type m: int
#         :type n: int
#         :type N: int
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         memo = {}
#         self.mod = 10 ** 9 + 7
#
#         def dfs(i, j, moves):
#             if (i, j, moves) in memo:
#                 return memo[(i, j, moves)]
#             ans = 0
#             if moves == N:
#                 return 0
#             if i == 0:
#                 ans += 1
#             if i == m - 1:
#                 ans += 1
#             if j == 0:
#                 ans += 1
#             if j == n - 1:
#                 ans += 1
#             ans %= self.mod
#             if i > 0:
#                 ans = (ans + dfs(i - 1, j, moves + 1)) % self.mod
#             if i < m - 1:
#                 ans = (ans + dfs(i + 1, j, moves + 1)) % self.mod
#             if j > 0:
#                 ans = (ans + dfs(i, j - 1, moves + 1)) % self.mod
#             if j < n - 1:
#                 ans = (ans + dfs(i, j + 1, moves + 1)) % self.mod
#             memo[(i, j, moves)] = ans
#             return ans
#
#         return dfs(i, j, 0)

class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = []
        for x in range(m):
            dp.append([0] * n)
        dp[i][j] = 1
        count = 0
        MOD = 1000000000 + 7
        for moves in range(N):
            temp = []
            for x in range(m):
                temp.append([0] * n)
            for i in range(0, m):
                for j in range(0, n):
                    if i == 0:
                        count = (count + dp[i][j]) % MOD
                    if i == m - 1:
                        count = (count + dp[i][j]) % MOD
                    if j == 0:
                        count = (count + dp[i][j]) % MOD
                    if j == n - 1:
                        count = (count + dp[i][j]) % MOD
                    temp[i][j] = ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % MOD
                    temp[i][j] += ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % MOD
                    temp[i][j] %= MOD
            dp = temp
        return count


sol = Solution()
print(sol.findPaths(3,
                    2,
                    5,
                    1,
                    1))
