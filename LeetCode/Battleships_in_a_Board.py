class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                top = board[i - 1][j] if i > 0 else '.'
                left = board[i][j - 1] if j > 0 else '.'
                if board[i][j] == 'X' and top != 'X' and left != 'X':
                    ans += 1
        return ans


so = Solution()
print(so.countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
