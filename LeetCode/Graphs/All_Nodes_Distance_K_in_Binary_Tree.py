# Definition for a binary tree node.
# class TreeNode:


class ParentNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        newRoot = None
        newTarget = None

        def check(root, parent):
            temp = ParentNode(root.val)
            temp.parent = parent
            if target == root.val:
                newTarget = temp
            if root.left:
                temp.left = check(root.left, temp)
            if root.right:
                temp.right = check(root.right, temp)

            return temp

        elems = []

        def traverse(node, k):
            if K == k:
                elems.append(node.val)
                return
            if node.parent:
                traverse(node.parent, k + 1)
            if node.left:
                traverse(node.left, k + 1)
            if node.right:
                traverse(node.right, k + 1)

        traverse(newTarget)
        return elems
