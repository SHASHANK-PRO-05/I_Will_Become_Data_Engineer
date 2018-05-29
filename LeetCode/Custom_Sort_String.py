class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        index = dict()

        for i in range(0, len(T)):
            index[T[i]] = i

        class customKeys:
            def __init__(self, elem):
                self.elem = elem
                if elem not in index:
                    index[elem] = -1

            def __gt__(self, other):
                return index[self.elem] > index[other.elem]

            def __lt__(self, other):
                return index[self.elem] < index[other.elem]

            def __eq__(self, other):
                return index[self.elem] == index[other.elem]

            def __str__(self):
                return self.elem

        keys = [None] * len(T)
        for i in range(0, len(T)):
            keys[i] = customKeys(T[i])
        keys = sorted(keys)
        ans = []
        for key in keys:
            ans.append(key.elem)
        return ''.join(ans)


sol = Solution()
print(sol.customSortString("cba", "dcba"))
