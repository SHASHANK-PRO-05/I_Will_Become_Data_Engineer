from bisect import *


class MyCalendarThree:

    def __init__(self):
        self.X = [0, 10 ** 9]
        self.value = [0, 0]
        self.m = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """

        def index(x):
            i = bisect_left(self.X, x)

            if not self.X[i] == x:
                self.X.insert(i, x)
                self.value.insert(i, self.value[i - 1])
            return i

        i = index(start)
        j = index(end)
        for temp in range(i, j):
            self.value[temp] += 1
        self.m = max(max(self.value[i:j]), self.m)
        return self.m

    # Your MyCalendarThree object will be instantiated and called as such:


# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

sol = MyCalendarThree()
sol.book(10, 20)
sol.book(50, 60)
sol.book(10, 40)
sol.book(5, 15)
sol.book(5, 10)
sol.book(25, 55)
