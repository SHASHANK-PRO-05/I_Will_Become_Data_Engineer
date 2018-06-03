class Solution:
    def pushDominoes(self, dominoes):
        ansStr = ''
        n = len(dominoes)
        listL = [n] * n
        listR = [n] * n
        prevL = n
        prevR = n
        for i in range(0, n):
            if dominoes[i] == 'R':
                listR[i] = 0
                prevR = 0
            elif dominoes[i] == 'L':
                listR[i] = n
                prevR = n
            else:
                listR[i] = min(prevR + 1, n)
                prevR = listR[i]

        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                listL[i] = 0
                prevL = 0
            elif dominoes[i] == 'R':
                listL[i] = n
                prevL = n
            else:
                listL[i] = min(prevL + 1, n)
                prevL = listL[i]

        for i in range(0, n):
            if listL[i] > listR[i]:
                ansStr += 'R'
            elif listL[i] < listR[i]:
                ansStr += 'L'
            else:
                ansStr += '.'
        return ansStr


sol = Solution()
print(sol.pushDominoes("LL.R"))
