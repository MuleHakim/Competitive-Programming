class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        numOfMagicSquare = 0

        def magic(a,b,c,d,e,f,x,y,z):
            
            rowSum1 = a + b + c
            rowSum2 = d + e + f
            rowSum3 = x + y + z
            colSum1 = a + d + x
            colSum2 = b + e + y
            colSum3 = c + f + z
            diagSum = a + e + z
            antiDiagSum = c + e + x

            return rowSum1 == rowSum2 == rowSum3 == colSum1 == colSum2 == colSum3 == diagSum == antiDiagSum

        check = {1,2,3,4,5,6,7,8,9}
        for row in range(n - 2):
            for col in range(m - 2):
                tempSet = set()
                tempSet.update([grid[row][col], grid[row][col+1], grid[row][col+2]])
                tempSet.update([grid[row+1][col], grid[row+1][col+1], grid[row+1][col+2]])
                tempSet.update([grid[row+2][col], grid[row+2][col+1], grid[row+2][col+2]])

                if tempSet == check and magic(grid[row][col],grid[row][col+1], grid[row][col+2], \
                                                grid[row+1][col], grid[row+1][col+1], grid[row+1][col+2], \
                                                grid[row+2][col], grid[row+2][col+1], grid[row+2][col+2]):
                    numOfMagicSquare += 1

        return numOfMagicSquare

