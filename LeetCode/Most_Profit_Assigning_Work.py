class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        self.zipped = sorted(zip(difficulty, profit))
        self.worker = worker
        ans = 0
        maxima = [self.zipped[0][1]] * len(self.zipped)
        currentMaxima = maxima[0]

        for i in range(1, len(self.zipped)):
            currentMaxima = max(currentMaxima, self.zipped[i][1])
            maxima[i] = currentMaxima

        for i, w in enumerate(worker):
            lower = self.checkLowerBound(w)
            if lower != -1:
                ans = ans + maxima[lower]
        return ans

    def checkLowerBound(self, level):
        start = 0
        end = len(self.zipped) - 1
        ans = -1
        while start <= end:
            mid = int((start + end) / 2)
            if self.zipped[mid][0] <= level:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


sol = Solution()
print(sol.maxProfitAssignment([85, 47, 57],
                              [24, 66, 99],
                              [40, 25, 25]))
