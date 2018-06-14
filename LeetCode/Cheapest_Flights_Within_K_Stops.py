from collections import deque


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = []
        for i in range(0, n):
            graph.append([])
        for i in range(0, len(flights)):
            graph[flights[i][0]].append([flights[i][1], flights[i][2]])

        memo = {src: 0}
        d = deque([(src, 0, 0)])

        while d:
            elem = d.popleft()

            if elem[1] <= K:
                for child in graph[elem[0]]:

                    if child[0] not in memo or memo[child[0]] > elem[2] + child[1]:
                        d.append((child[0], elem[1] + 1, elem[2] + child[1]))
                        memo[child[0]] = elem[2] + child[1]

        if dst not in memo:
            return -1
        else:
            return memo[dst]


sol = Solution()
print(sol.findCheapestPrice(3,
                            [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                            0,
                            2,
                            1))
