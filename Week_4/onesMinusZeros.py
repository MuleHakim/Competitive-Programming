class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        diffMatrix = [[0] * n for _ in range(m)]
        onesRow = [row.count(1) for row in grid]
        onesCol = [col.count(1) for col in zip(*grid)]

        for index1 in range(m):
            for index2 in range(n):
                diffMatrix[index1][index2] = onesRow[index1] + onesCol[index2] - (n - onesRow[index1]) - (m - onesCol[index2])
                            
        return diffMatrix

