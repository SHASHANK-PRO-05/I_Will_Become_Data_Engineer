from collections import deque


class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        q = deque()
        array = [0] * (len(A) + 1)
        ans = len(A) + 1
        for i in range(1, len(A) + 1):
            array[i] = array[i - 1] + A[i - 1]

        for i in range(len(array)):
            while q and array[q[-1]] >= array[i]:
                q.pop()
            while q and array[i] - array[q[0]] >= K:
                ans = min(ans, i - q[0])
                q.popleft()
            q.append(i)

        return -1 if ans == len(A) + 1 else ans
