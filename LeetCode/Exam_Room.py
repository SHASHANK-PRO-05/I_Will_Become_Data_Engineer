class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.L = [(0, N - 1)]

    def seat(self):
        """
        :rtype: int
        """
        index = 0
        max_dist = -1
        cur_index = -1
        for i in range(0, len(L)):
            elem = self.L[i]
            left = elem[0] - 1
            right = elem[0] + 1
            if left < 0:
                temp_dist = right
                if temp_dist > max_dist:
                    cur_index = 0
                    index = i

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
