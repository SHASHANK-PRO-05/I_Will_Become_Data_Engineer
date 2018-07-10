from collections import defaultdict


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        dict = defaultdict(lambda: -1)

        def color(node, nodeChange):
            if dict[node] != -1:
                if dict[node] != nodeChange:
                    return False
                else:
                    return True
            dict[node] = nodeChange
            for i in range(0, len(graph[node])):
                if not color(graph[node][i], (nodeChange + 1) % 2):
                    return False
            return True

        for i in range(0, len(graph)):
            if dict[i] == -1:
                if not color(i, 0):
                    return False
        return True


sol = Solution()
print(sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
