from collections import deque


class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        [x, y] = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        def utility(i, j):
            (row, col), directions = (i, j), ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))

            return sum([board[row + r][col + c] == 'M' for r, c in directions if
                        0 <= row + r < len(board) and 0 <= col + c < len(board[0])])

        def traverse_neighbours(i, j):
            m, n = len(board), len(board[i])
            empties = []
            if i > 0 and board[i - 1][j] == 'E':
                empties.append((i - 1, j))
            if j > 0 and board[i][j - 1] == 'E':
                empties.append((i, j - 1))
            if i < m - 1 and board[i + 1][j] == 'E':
                empties.append((i + 1, j))
            if j < n - 1 and board[i][j + 1] == 'E':
                empties.append((i, j + 1))
            if i > 0 and j > 0 and board[i - 1][j - 1] == 'E':
                empties.append((i - 1, j - 1))
            if i > 0 and j < n - 1 and board[i - 1][j + 1] == 'E':
                empties.append((i - 1, j + 1))
            if i < m - 1 and j < n - 1 and board[i + 1][j + 1] == 'E':
                empties.append((i + 1, j + 1))
            if i < m - 1 and j > 0 and board[i + 1][j - 1] == 'E':
                empties.append((i + 1, j - 1))
            return empties

        q = deque([(x, y)])
        while q:
            (i, j) = q.popleft()
            count = utility(i, j)
            if count != 0:
                board[i][j] = str(count)
            else:
                board[i][j] = 'B'
                q.extendleft(traverse_neighbours(i, j))

        return board
