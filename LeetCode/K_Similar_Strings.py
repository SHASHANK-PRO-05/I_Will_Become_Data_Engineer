from collections import deque


class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        q = deque()
        q.append((0, 0, list(A), list(B)))
        while q:
            elem = q.popleft()
            if elem[2] == elem[3]:
                return elem[1]

            for i in range(elem[0], len(elem[2])):
                if elem[2][i] != elem[3][i]:
                    break
            for j in range(i + 1, len(elem[2])):
                if elem[3][i] == elem[2][j]:
                    elem
                    q.append((i + 1, elem[1] + 1,
                              elem[2][0: j] + [elem[2][i]] + elem[2][
                                                             j + 1: len(elem[2])],
                              elem[3]))


sol = Solution()
print(sol.kSimilarity("aaaabbbbccccddddeeee",
                      "cdddbbcacbeedcebaeaa"))
