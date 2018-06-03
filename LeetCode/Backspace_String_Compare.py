class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        listS = []
        for i, s in enumerate(S):
            if s == '#':
                if len(listS) != 0:
                    listS.pop()
            else:
                listS.append(s)
        listT = []
        for i, t in enumerate(T):
            if t == '#':
                if len(listT) != 0:
                    listT.pop()
            else:
                listT.append(t)
        return listT == listS


sol = Solution()
print(sol.backspaceCompare("a#c", "c"))
