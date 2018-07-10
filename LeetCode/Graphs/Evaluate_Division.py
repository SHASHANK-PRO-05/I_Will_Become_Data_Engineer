from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        map = defaultdict(lambda: [])
        visited = defaultdict(lambda: False)
        for i in range(len(equations)):
            k = equations[i]
            map[k[0]].append((k[1], values[i]))
            map[k[1]].append((k[0], 1 / values[i]))

        ans = [0] * len(queries)

        def find(node, dst, P):
            if node == dst:
                return P
            l = map[node]
            if len(l) == 0:
                return -1
            for i in range(len(l)):
                if not visited[l[i][0]]:
                    visited[l[i][0]] = True
                    temp_ans = find(l[i][0], dst, P * l[i][1])
                    visited[l[i][0]] = False
                    if not temp_ans == -1:
                        return temp_ans

            return -1

        for i in range(len(queries)):
            visited[queries[i][0]] = True
            ans[i] = find(queries[i][0], queries[i][1], 1)
            visited[queries[i][0]] = False
        return ans
