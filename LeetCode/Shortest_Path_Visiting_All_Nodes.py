class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)
        dist = [[float('inf')] * n for i in range(0, 1 << n)]
        for x in range(0, n):
            dist[1 << x][x] = 0

        for cover in range(0, 1 << n):
            repeat = True
            while repeat:
                repeat = False
                for head, d in enumerate(dist[cover]):
                    for elem in graph[head]:
                        cover2 = cover | 1 << elem
                        if d + 1 < dist[cover2][elem]:
                            dist[cover2][elem] = d + 1
                            if cover2 == cover:
                                repeat = True

        return min(dist[2 ** n - 1])


sol = Solution()
print(sol.shortestPathLength(
    [[1, 4], [0, 3, 4, 7, 9], [6, 10], [1, 10], [1, 0], [6], [7, 2, 5], [6, 1, 8], [7], [1], [2, 3]]))
