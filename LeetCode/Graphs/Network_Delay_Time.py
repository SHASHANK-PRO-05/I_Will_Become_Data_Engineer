from collections import defaultdict, deque


class Solution:
    def networkDelayTime(self, time, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(lambda: [])
        bfs = deque()
        memo = defaultdict(lambda: float('inf'))
        for i in range(0, len(time)):
            times = time[i]
            graph[times[0]].append((times[1], times[2]))
            if times[0] == K:
                bfs.append((times[1], times[2]))

        memo[K] = 0

        ans = float('-inf')

        while bfs:
            elem = bfs.popleft()
            if memo[elem[0]] > elem[1]:
                memo[elem[0]] = elem[1]
                for i in range(0, len(graph[elem[0]])):
                    addElem = graph[elem[0]][i]
                    bfs.append((addElem[0], elem[1] + addElem[1]))

        for i in range(1, N + 1):
            ans = max(ans, memo[i])

        return ans if ans < float('inf') else -1


sol = Solution()
print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1]],
                           4,
                           2))
