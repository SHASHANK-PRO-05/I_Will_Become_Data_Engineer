# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxlevel = -1
        currentValue = -1

        def checkLeft(node, level):
            if node == None:
                return
            if level > maxlevel:
                maxlevel = level
                currentValue = node.val
            checkLeft(node.left, level + 1)
            checkLeft(node.right, level + 1)

        checkLeft(root, 0)
        return currentValue


sol = Solution()
print(sol.findBottomLeftValue())
