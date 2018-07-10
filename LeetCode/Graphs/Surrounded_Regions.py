import collections


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        queue = collections.deque()

        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        memo = []
        for i in range(0, n):
            memo.append([False] * m)
        for i in range(0, n):
            if board[i][0] == 'O' and not memo[i][0]:
                queue.append((i, 0))
                memo[i][0] = True
            if board[i][m - 1] == 'O' and not memo[i][m - 1]:
                queue.append((i, m - 1))
                memo[i][m - 1] = True

        for i in range(0, m):
            if board[0][i] == 'O' and not memo[0][i]:
                queue.append((0, i))
                memo[0][i] = True
            if board[n - 1][i] == 'O' and not memo[n - 1][i]:
                queue.append((n - 1, i))
                memo[n - 1][i] = True

        while queue:
            elem = queue.popleft()
            print(elem)
            if elem[0] - 1 >= 0 and board[elem[0] - 1][elem[1]] == 'O' and not memo[elem[0] - 1][elem[1]]:
                queue.append((elem[0] - 1, elem[1]))
                memo[elem[0] - 1][elem[1]] = True
            if elem[0] + 1 < n and board[elem[0] + 1][elem[1]] == 'O' and not memo[elem[0] + 1][elem[1]]:
                queue.append((elem[0] + 1, elem[1]))
                memo[elem[0] + 1][elem[1]] = True
            if elem[1] - 1 >= 0 and board[elem[0]][elem[1] - 1] == 'O' and not memo[elem[0]][elem[1] - 1]:
                queue.append((elem[0], elem[1] - 1))
                memo[elem[0]][elem[1] - 1] = True
            if elem[1] + 1 < m and board[elem[0]][elem[1] + 1] == 'O' and not memo[elem[0]][elem[1] + 1]:
                queue.append((elem[0], elem[1] + 1))
                memo[elem[0]][elem[1] + 1] = True

        for i in range(0, n):
            for j in range(0, m):
                if not memo[i][j]:
                    board[i][j] = 'X'


sol = Solution()
print(sol.solve([["O", "O"], ["O", "O"]]))
