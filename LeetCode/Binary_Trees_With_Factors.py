import math


class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        A = sorted(A)
        d = {}
        ans = 0
        indexes = {}
        for i, a in enumerate(A):
            d[a] = 1
            indexes[a] = i
            l = self.lowerBound(A, int((math.sqrt(a))))
            for j in range(0, l + 1):
                if a % A[j] == 0 and a / A[j] in indexes.keys():
                    k = indexes[a / A[j]]
                    if j != k:
                        d[a] = (d[a] + d[A[j]] * d[A[k]] * 2) % mod
                    else:
                        d[a] = (d[a] + d[A[j]] * d[A[k]]) % mod
            ans = (ans + d[a]) % mod

        return ans

    def lowerBound(self, A, val):
        start = 0
        end = len(A) - 1
        ans = -1
        while start <= end:
            mid = int((start + end) / 2)
            if A[mid] <= val:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans


sol = Solution()
print(sol.numFactoredBinaryTrees([18, 3, 6, 2]))
