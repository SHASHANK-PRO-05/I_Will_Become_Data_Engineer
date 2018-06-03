class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        listLeft = [0] * len(A)
        listRight = [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                listLeft[i] = listLeft[i - 1] + 1
            else:
                listLeft[i] = 0
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                listRight[i] = listRight[i + 1] + 1
            else:
                listRight[i] = 0

        maxAns = 0
        for i in range(0, len(A)):
            if listLeft[i] != 0 or listRight[i] != 0:
                maxAns = max(maxAns, listRight[i] + listLeft[i] + 1)
        return maxAns


sol = Solution()
print(sol.longestMountain([2, 2, 2]))
