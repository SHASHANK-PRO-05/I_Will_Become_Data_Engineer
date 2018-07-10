import math


class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 2
        elif N == 2:
            return 2
        elif N == 3:
            return 3
        if N >= 9989900:
            return 100030001
        while True:
            string = str(N)
            if string == string[::-1]:
                if not any(N % i == 0 for i in range(2, int(math.ceil(N ** 0.5)) + 1)):
                    return N
            N = N + 1


def reverse(num, i, j):
    while (i < j):
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        i = i + 1
        j = j - 1


sol = Solution()
print(sol.primePalindrome(9989900))
