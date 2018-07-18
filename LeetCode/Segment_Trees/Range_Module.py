# This is not a segment tree question
from bisect import *


class RangeModule:

    def __init__(self):
        self.X = [0, 10 ** 9]
        self.track = [False, False]

    def addRange(self, left, right, track=True):
        """
        :type left: int
        :type right: int
        :rtype: void
        """

        def index(value):
            i = bisect_left(self.X, value)
            if not self.X[i] == value:
                self.X.insert(i, value)
                self.track.insert(i, self.track[i - 1])
            return i

        i = index(left)
        j = index(right)
        self.track[i:j] = [track]
        self.X[i:j] = [left]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect(self.X, left) - 1
        j = bisect_left(self.X, right)
        return all(self.track[i:j])

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.addRange(left, right, False)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
