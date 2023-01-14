class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroesRow = set()
        zeroesCol = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroesRow.add(row)
                    zeroesCol.add(col)

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and (row in zeroesRow or col in zeroesCol):
                    matrix[row][col] = 0

