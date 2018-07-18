import math


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            return
        size = int(math.ceil(math.log2(len(nums))))
        size = 2 * (2 ** size) - 1
        self.tree = [0] * size
        self.nums = nums

        def build(node, start, end):
            if start == end:
                self.tree[node] = nums[start]
            else:
                mid = int((start + end) / 2)
                build(node * 2 + 1, start, mid)
                build(node * 2 + 2, mid + 1, end)
                self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

        build(0, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if not self.tree:
            return

        def updateTree(node, start, end, i, val):
            if start == end:
                self.tree[node] = val
            else:
                mid = int((start + end) / 2)
                if start <= i and i <= mid:
                    updateTree(node * 2 + 1, start, mid, i, val)
                else:
                    updateTree(node * 2 + 2, mid + 1, end, i, val)
                self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

        updateTree(0, 0, len(self.nums) - 1, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.tree:
            return None

        def queryTree(node, start, end, i, j):
            if i > end or start > j:
                return 0
            elif i <= start and end <= j:
                return self.tree[node]
            else:
                mid = int((start + end) / 2)
                return queryTree(node * 2 + 1, start, mid, i, j) + queryTree(node * 2 + 2, mid + 1, end, i, j)

        return queryTree(0, 0, len(self.nums) - 1, i, j)
