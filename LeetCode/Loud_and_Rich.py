class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        graph = []
        visited = [False] * len(quiet)
        tempe = [None] * len(quiet)

        for i in range(0, len(quiet)):
            graph.append([])

        for i in range(0, len(richer)):
            graph[richer[i][1]].append(richer[i][0])

        def recur(node):
            if visited[node]:
                return tempe[node]
            ans = quiet[node]
            index = node
            for i in range(0, len(graph[node])):

                (temp, nIndex) = recur(graph[node][i])
                if temp < ans:
                    ans = temp
                    index = nIndex
            visited[node] = True

            tempe[node] = (ans, index)
            return ans, index

        finalAns = []
        for i in range(0, len(quiet)):
            finalAns.append(recur(i)[1])
        return finalAns


sol = Solution()
print(sol.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                      [3, 2, 5, 4, 6, 1, 7, 0]))
