class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        return self.treeParse(nums, 0, len(nums))

    def treeParse(self, nums, start, end):
        if end - start == 1:
            return TreeNode(nums[start])
        elif end != start:
            maxIndex = start
            maxValue = nums[start]
            for i in range(start + 1, end):
                if maxValue < nums[i]:
                    maxIndex = i
                    maxValue = nums[i]

            temp = TreeNode(nums[maxIndex])
            temp.left = self.treeParse(nums, start, maxIndex)
            temp.right = self.treeParse(nums, maxIndex + 1, end)
            return temp


if __name__ == "__main__":
    temp = Solution()
    print(temp.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
