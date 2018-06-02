class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.visited = {}
        self.rooms = rooms

        def visit(node):
            if node in self.visited.keys():
                return
            else:
                self.visited[node] = True
                list = self.rooms[node]
                for i in range(0, len(self.rooms[node])):
                    visit(self.rooms[node][i])

        visit(0)

        for i in range(0, len(rooms)):
            if i not in self.visited.keys():
                return False
        return True


sol = Solution()
print(sol.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
