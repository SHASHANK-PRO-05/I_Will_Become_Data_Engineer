import collections


class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        P = [0]
        ans = len(A) + 1
        for i in range(0, len(A)):
            P.append(P[-1] + A[i])
        deque = collections.deque()

        for i in range(0, len(P)):

            while deque and P[i] <= P[deque[-1]]:
                deque.pop()
            while deque and P[i] - P[deque[0]] >= K:
                ans = min(ans, i - deque[0])
                deque.popleft()
            deque.append(i)
        if ans == len(A) + 1:
            return -1
        else:
            return ans


sol = Solution()
print(sol.shortestSubarray([56, -21, 56, 35, -9],
                           61))
