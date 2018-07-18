class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = "{0:b}".format(N)
        i = 0
        ans = 0
        while i < len(binary) and binary[i] != '1':
            i = i + 1

        j = i + 1
        while j < len(binary):
            if binary[j] == '1':
                ans = max(ans, j - i)
                i = j
            j = j + 1
        return ans


sol = Solution()
print(sol.binaryGap(8))
