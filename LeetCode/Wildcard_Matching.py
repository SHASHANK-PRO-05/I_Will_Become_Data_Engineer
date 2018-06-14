class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        array = []
        for i in range(0, len(s) + 1):
            temp = []
            for j in range(0, len(p) + 1):
                temp.append(False)
            array.append(temp)

        array[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                array[0][i] = array[0][i - 1]

        for i in range(0, len(s)):
            for j in range(0, len(p)):

                if s[i] == p[j] or p[j] == '?':
                    array[i + 1][j + 1] = array[i][j]
                elif p[j] == '*':
                    if array[i][j] or array[i][j + 1] or array[i + 1][j]:
                        array[i + 1][j + 1] = True
                    # array[i + j][j + 1] = (array[i][j]  array[i + 1][j] | array[i][j + 1] | array[i + 1][j + 1])
                    # print(array[i][j], array[i + 1][j], array[i][j + 1], array[i + 1][j + 1])

        return array[len(s)][len(p)]


sol = Solution()
print(sol.isMatch("aa", "a*"))
