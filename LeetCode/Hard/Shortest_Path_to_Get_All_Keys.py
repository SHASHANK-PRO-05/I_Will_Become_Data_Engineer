from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        def check(elem, S):
            if elem == '.' or elem == '@' or elem.islower() or elem.lower() in S:
                return True
            else:
                return False

        x, y = 0, 0
        m, n = len(grid), len(grid[0])
        number_of_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    x = i
                    y = j
                if grid[i][j].islower():
                    number_of_keys += 1
        queue = deque([(x, y, set(), 0)])
        sizeCheck = []
        for i in range(m):
            sizeCheck.append([None] * n)
        while queue:
            (i, j, s, moves) = queue.popleft()

            if not sizeCheck[i][j] == None and len(s.difference(sizeCheck[i][j])) == 0:
                continue
            sizeCheck[i][j] = s
            if len(s) == number_of_keys:
                return moves

            if i < m - 1 and check(grid[i + 1][j], s):
                new_s = s.copy()
                if grid[i + 1][j].islower():
                    new_s.add(grid[i + 1][j])
                queue.append((i + 1, j, new_s, moves + 1))

            if i > 0 and check(grid[i - 1][j], s):
                new_s = s.copy()
                if grid[i - 1][j].islower():
                    new_s.add(grid[i - 1][j])
                queue.append((i - 1, j, new_s, moves + 1))

            if j > 0 and check(grid[i][j - 1], s):
                new_s = s.copy()
                if grid[i][j - 1].islower():
                    new_s.add(grid[i][j - 1])
                queue.append((i, j - 1, new_s, moves + 1))

            if j < n - 1 and check(grid[i][j + 1], s):
                new_s = s.copy()
                if grid[i][j + 1].islower():
                    new_s.add((grid[i][j + 1]))
                queue.append((i, j + 1, new_s, moves + 1))

        return -1


sol = Solution()
print(sol.shortestPathAllKeys(["@#....", ".Aabcd", ".BCD.."]))
