class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        graph = []
        for i in range(0, len(quiet)):
            graph.append([i])
        for i in range(0, len(richer)):
            graph[richer[i][1]].append(richer[i][0])

        ans = [-1] * len(quiet)

        def find(node):
            if ans[node] != -1:
                return ans[node]
            node_min = graph[node][0]
            for i in range(1, len(graph[node])):
                temp_min = find(graph[node][i])
                if quiet[node_min] > quiet[temp_min]:
                    node_min = temp_min
            ans[node] = node_min
            return ans[node]

        for i in range(0, len(quiet)):
            if ans[i] == -1:
                find(i)
        return ans


sol = Solution()
print(sol.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 0]))
