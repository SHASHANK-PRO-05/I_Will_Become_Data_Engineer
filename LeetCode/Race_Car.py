class Solution:
    def __init__(self):
        self.d = {}
        self.d[1] = 1

    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.d:
            return self.d[target]
        n = target.bit_length()
        if 2 ** n - 1 == target:
            self.d[target] = n
            return n
        self.d[target] = self.racecar(2 ** n - 1 - target) + n + 1
        for i in range(0, n - 1):
            self.d[target] = min(self.d[target], self.racecar(target - (2 ** (n - 1)) + 2 ** i) + n + 1 + i)
        return self.d[target]
