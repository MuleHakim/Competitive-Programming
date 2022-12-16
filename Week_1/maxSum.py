class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        max_sum = -math.inf
        for i in range(r-2):
            for j in range(c-2):
                sum_ = (grid[i][j] + grid[i][j + 1] + grid[i][j + 2]) + (grid[i + 1][j + 1]) +(grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2])
                max_sum = max(max_sum,sum_)
        return max_sum
