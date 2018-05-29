# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.maxLevel = -1

        def check(node, level):
            if node == None:
                return
            else:
                if level > self.maxLevel:
                    list.append(node.val)
                    self.maxLevel = level
                else:
                    list[level] = max(list[level], node.val)
                check(node.left, level + 1)
                check(node.right, level + 1)

        check(root, 0)
        return list
