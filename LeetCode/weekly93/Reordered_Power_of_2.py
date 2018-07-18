from collections import Counter


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        string = Counter(str(N))
        num = 1
        list = []
        while num <= 10 ** 9:
            tempCounter = Counter(str(num))
            if tempCounter == string and len(str(N)) == len(str(num)):
                return True

            num = num * 2
        return False


sol = Solution()
print(sol.reorderedPowerOf2(1))
