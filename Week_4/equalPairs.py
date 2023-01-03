class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        output = 0
        length = len(grid)

        for indexCol in range(length):

            column = []
            for indexRow in range(length):
                column.append(grid[indexRow][indexCol])

            if column in grid:
                output += grid.count(column)

        return output

