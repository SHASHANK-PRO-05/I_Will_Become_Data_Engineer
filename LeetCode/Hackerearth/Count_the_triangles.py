class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.count = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif root.val > key:
            root.left = self.insert(root.left, key)
        elif root.val == key:
            root.count += 1
            return root
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + (max(self.getHeight(root.right), self.getHeight(root.left)))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        elif balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        elif balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        else:
            return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            root.count -= 1
            if root.count > 0:
                return root
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.giveMinValue(root.right)
            root.val = temp.val
            root.count = temp.count
            temp.count = 0
            root.right = self.delete(root.right, temp.val)
        if root is None:
            return root

        root.height = 1 + (max(self.getHeight(root.right), self.getHeight(root.left)))
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def giveMinValue(self, root):
        if root == None or root.left == None:
            return root
        return self.giveMinValue(root.left)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        x = y.right

        y.right = z
        z.left = x

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.right), self.getHeight(y.left))
        return y

    def preOrder(self, root):

        if not root:
            return "None"
        string = "{" + self.preOrder(root.left) + "<-" + str(root.val) + ":" + str(root.count) + "->" + self.preOrder(
            root.right) + "}"
        return string

    def giveMaxima(self, root):
        if root == None or root.right == None:
            return root
        return self.giveMaxima(root.right)

    def min2s(self, root):
        list = []

        def check(root):
            if root == None:
                return
            if len(list) == 2:
                return
            check(root.left)
            if len(list) == 2:
                return
            list.append(root.val)
            if len(list) == 2:
                return
            if root.count > 1:
                list.append(root.val)
            check(root.right)

        check(root)
        return list

    def checkWithCurr(self, root, val):
        maxima = self.giveMaxima(root)
        minima = self.min2s(root)
        if len(minima) < 2:
            return True
        MAX = maxima.val
        MIN_1 = minima[0]
        MIN_2 = minima[1]

        if MIN_1 + MIN_2 >= val and MIN_2 + val >= MIN_1 and MIN_1 + val >= MIN_2 and MAX + MIN_1 >= val and MAX + val >= MIN_1 and val + MIN_1 >= MAX:
            return True
        else:
            return False





def start_simulation(l=None):
    n = int(input())
    if not l:
        array = list(map(lambda x: int(x), input().split(" ")))
    else:
        array = l
    ans = 2 * n - 1
    i = 0
    tree = AVLTree()
    root = tree.insert(None, array[0])

    for j in range(1, len(array)):

        while not tree.checkWithCurr(root, array[j]) and i < j - 1:
            ans += max((j - i - 2), 0)
            root = tree.delete(root, array[i])
            i = i + 1

        root = tree.insert(root, array[j])
    j = j + 1
    while i < j:
        ans += max((j - i - 2), 0)
        i = i + 1

    print(ans)


# from random import randint
#
# list = []
# for i in range(0, 100):
#     list.append(randint(0, 1000000000))
# print(100)
# print(''.join(str(x) + " " for x in list))
# start_simulation(list)
start_simulation()
