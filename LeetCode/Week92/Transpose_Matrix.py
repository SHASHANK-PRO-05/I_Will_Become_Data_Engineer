class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        if n == 0:
            return A
        m = len(A[0])
        if m == 0:
            return A
        new_A = []
        for i in range(0, m):
            new_A.append([0] * n)

        for i in range(0, n):
            for j in range(0, m):
                new_A[j][i] = A[i][j]

        return new_A
