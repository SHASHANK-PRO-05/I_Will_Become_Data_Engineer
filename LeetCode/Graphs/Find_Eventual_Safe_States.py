from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        memo = {}
        ans = []
        visited = defaultdict(lambda: False)

        def isCircleThere(node):
            if node in memo:
                return memo[node]
            ans = True
            for i in range(0, len(graph[node])):
                if not visited[graph[node][i]]:
                    visited[graph[node][i]] = True
                    ans = ans and isCircleThere(graph[node][i])
                    visited[graph[node][i]] = False
                else:
                    memo[node] = False
                    return False

            memo[node] = ans
            return ans

        for i in range(0, len(graph)):
            if isCircleThere(i):
                ans.append(i)
        return ans


def test():
    sol = Solution()
    print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))


test()
