class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        visited = [False] * n

        def check(node):
            if node == n - 1:
                return [[n - 1]]
            elif visited[node]:
                return None
            else:
                visited[node] = True
                temp = None
                for i in range(0, len(graph[node])):
                    tempList = check(graph[node][i])
                    if tempList != None:
                        if temp == None:
                            temp = []
                        for l in tempList:
                            temp.append([node] + l)
                visited[node] = False
                return temp

        return check(0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.allPathsSourceTarget([[1, 2], [3], [3], []]))
