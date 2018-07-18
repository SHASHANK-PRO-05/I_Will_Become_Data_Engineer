import math


class SegmentTree:
    def __init__(self, size):
        self.size = size - 1
        size = int(math.ceil(math.log2(size)))
        size = 2 ** (size + 1) - 1
        self.tree = [0] * size
        self.lazy = [0] * size

    def _query(self, node, start, end, L, R):
        if self.lazy[node] != 0:
            self.tree[node] = self.lazy[node]
            if node * 2 + 1 < len(self.tree):
                self.lazy[node * 2 + 1] = self.lazy[node]
            if node * 2 + 2 < len(self.tree):
                self.lazy[node * 2 + 2] = self.lazy[node]
            self.lazy[node] = 0
        if L > end or start > R:
            return float('-inf')
        elif L <= start and end <= R:
            return self.tree[node]
        else:
            mid = int((start + end) / 2)
            ans = float('-inf')
            if node * 2 + 1 < len(self.tree):
                ans = max(ans, self._query(node * 2 + 1, start, mid, L, R))
            if node * 2 + 2 < len(self.tree):
                ans = max(ans, self._query(node * 2 + 2, mid + 1, end, L, R))
            return ans

    def query(self, L, R):
        return self._query(0, 0, self.size, L, R)

    def _update(self, node, start, end, L, R, value):
        if self.lazy[node] != 0:
            self.tree[node] = self.lazy[node]
            if node * 2 + 1 < len(self.tree):
                self.lazy[node * 2 + 1] = self.lazy[node]
            if node * 2 + 2 < len(self.tree):
                self.lazy[node * 2 + 2] = self.lazy[node]
            self.lazy[node] = 0
        if L > end or R < start:
            return float('-inf')
        if L <= start and end <= R:
            self.tree[node] = value
            if node * 2 + 1 < len(self.tree):
                if node * 2 + 1 < len(self.tree):
                    self.lazy[node * 2 + 1] = value
                if node * 2 + 2 < len(self.tree):
                    self.lazy[node * 2 + 2] = value
            return self.tree[node]
        else:
            mid = int((start + end) / 2)
            ans = self.tree[node]
            if node * 2 + 1 < len(self.tree):
                ans = max(ans, self._update(node * 2 + 1, start, mid, L, R, value))
            if node * 2 + 2 < len(self.tree):
                ans = max(ans, self._update(node * 2 + 2, mid + 1, end, L, R, value))
            self.tree[node] = ans
            return self.tree[node]

    def update(self, L, R, value):
        self._update(0, 0, self.size, L, R, value)


class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if len(positions) == 0:
            return []
        coords = set()
        for i in range(len(positions)):
            left, size = positions[i]
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}
        tree = SegmentTree(len(index))
        ans = [0] * len(positions)
        best = 0
        for i in range(len(positions)):
            L, R = index[positions[i][0]], index[positions[i][0] + positions[i][1] - 1]
            h = tree.query(L, R) + positions[i][1]
            best = max(best, h)
            ans[i] = best
            tree.update(L, R, h)

        return ans


sol = Solution()
print(sol.fallingSquares([[9, 7], [1, 9], [3, 1]]))
