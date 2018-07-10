class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = dp(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
            memo[(i, j)] = ans
            return ans

        return dp(0, len(s) - 1)


import random
import string


def testCase():
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
    sol = Solution()
    print(s)
    print(sol.strangePrinter(s))


testCase()
