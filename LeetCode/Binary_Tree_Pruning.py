# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasOnes(self, node):
        if node == None:
            return False
        oneFound = False
        if node.val == 1:
            oneFound = True
        leftAns = self.hasOnes(node.left)
        if not leftAns:
            node.left = None
        rightAns = self.hasOnes(node.right)
        if not rightAns:
            node.right = None
        oneFound = oneFound or leftAns or rightAns
        return oneFound

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = self.hasOnes(root)
        if ans:
            return root
        else:
            return None
