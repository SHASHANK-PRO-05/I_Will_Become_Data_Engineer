import sys


class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        left = [sys.maxsize + 1] * n
        right = [sys.maxsize + 1] * n
        curRight = sys.maxsize + 1
        curLeft = sys.maxsize + 1
        for i in range(0, len(dominoes)):
            if dominoes[i] == 'R':
                curRight = 0
                right[i] = 0
            elif dominoes[i] == 'L':
                curRight = sys.maxsize + 1
                right[i] = sys.maxsize + 1
            else:
                curRight = curRight + 1
                right[i] = min(curRight, sys.maxsize + 1)

        for j in range(len(dominoes) - 1, -1, -1):
            if dominoes[j] == 'L':
                curLeft = 0
                left[j] = 0
            elif dominoes[j] == 'R':
                curLeft = sys.maxsize + 1
                left[j] = sys.maxsize + 1
            else:
                curLeft = curLeft + 1
                left[j] = min(curLeft, sys.maxsize + 1)

        list = [None] * n

        for i in range(0, n):
            if left[i] < right[i]:
                list[i] = 'L'
            elif left[i] > right[i]:
                list[i] = 'R'
            else:
                list[i] = dominoes[i]
        return ''.join(x for x in list)


sol = Solution()
print(sol.pushDominoes("LL.RR.LLRRLL.."))
