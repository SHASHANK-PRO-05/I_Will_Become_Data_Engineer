# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dict = defaultdict(lambda: [])

        self.maxDepth = 0

        def findDepth(node, level):
            if node == None:
                return
            self.maxDepth = max(self.maxDepth, level)
            dict[level].append(node)
            findDepth(node.left, level + 1)
            findDepth(node.right, level + 1)

        findDepth(root, 0)
        self.ans = None

        def createList(node, level):
            if node == None:
                return None
            if level == self.maxDepth:
                if dict[self.maxDepth] != [node]:
                    return [node]
                else:
                    self.ans = [node]
                    return None
            thisAns = []
            left = createList(node.left, level + 1)
            if left != None:
                thisAns += left
            left = createList(node.right, level + 1)
            if left != None:
                thisAns += left
            if thisAns == dict[self.maxDepth]:
                self.ans = node
                return None
            else:
                return thisAns

        createList(root, 0)
        return self.ans
