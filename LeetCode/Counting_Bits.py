class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        array = [0] * (num + 1)
        for i in range(1, num + 1):
            array[i] = (array[int(i / 2)] + (1 if i % 2 == 1 else 0))
        return array


so = Solution()
print(so.countBits(2))
