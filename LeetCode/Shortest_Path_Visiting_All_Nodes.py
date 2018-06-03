import sys


class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if len(graph) == 0:
            return 0
        self.graph = list(map(lambda x: set(x), graph))
        self.visits = [0] * len(graph)
        self.seti = set()
        self.minLen = sys.maxsize
        for i in range(0, len(graph)):
            self.check(i, 0)
        return self.minLen - 1

    def check(self, node, thisLen):

        if len(self.seti) == len(self.graph):
            self.minLen = min(self.minLen, thisLen)
            return
        else:

            for i in self.graph[node]:
                if i not in self.seti:
                    self.seti.add(i)
                self.visits[i] += 1
                self.graph[node].remove(i)
                self.check(i, thisLen + 1)
                self.graph[node].add(i)
                self.visits[i] -= 1
                if self.visits[i] == 0:
                    self.seti.remove(i)


sol = Solution()
print(sol.shortestPathLength(
    [[1, 4], [0, 3, 4, 7, 9], [6, 10], [1, 10], [1, 0], [6], [7, 2, 5], [6, 1, 8], [7], [1], [2, 3]]))
