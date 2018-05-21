class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        mcs = list(map(max, *grid))
        mrs = list(map(max, grid))
        ans = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                ans += (min(mcs[j], mrs[i]) - grid[i][j])
        return ans


if __name__ == "__main__":
    temp = Solution()
    print(temp.maxIncreaseKeepingSkyline([[3, 0, 8, 4],
                                          [2, 4, 5, 7],
                                          [9, 2, 6, 3],
                                          [0, 3, 1, 0]]))
