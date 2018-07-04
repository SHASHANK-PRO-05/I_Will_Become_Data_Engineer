class TreeNode:
    def _init_(self, x):
        self.val = x
        self.left = self.right = None


def merge(root1, root2):
    """
    Write your code here
    :type tree1: TreeNode
    :type tree2: TreeNode
    :rtype: TreeNode
    """
    inorder1 = check(root1, [])
    inorder2 = check(root2, [])
    newInorder = []

    i = 0
    j = 0

    while i < len(inorder1) and j < len(inorder2):
        if inorder1[i].val < inorder2[j].val:
            newInorder.append(inorder1[i])
            i += 1
        else:
            newInorder.append(inorder2[j])
            j += 1
        newInorder[-1].left = newInorder[-1].right = None

    while i < len(inorder1):
        newInorder.append(inorder1[i])
        i += 1
        newInorder[-1].left = newInorder[-1].right = None
    while j < len(inorder2):
        newInorder.append(inorder2[j])
        j += 1
        newInorder[-1].left = newInorder[-1].right = None
    return recursiveBuild(newInorder, 0, len(newInorder) - 1)


def recursiveBuild(list, start, end):
    if start > end:
        return None
    mid = int((start + end) / 2)
    node = list[mid]
    node.left = recursiveBuild(list, start, mid - 1)
    node.rigt = recursiveBuild(list, mid + 1, end)
    return node


def check(node, L):
    if not node:
        return L
    L = check(node.left, L)
    L.append(node)
    L = check(node.right, L)
    return L


