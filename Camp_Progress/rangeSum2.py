class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        
        self.prefix = []
        total = [0] * (m + 1)
        self.prefix.append(total)

        for i in range(n):
            for j in range(m):
                total[j+1] += matrix[i][j] + total[j] - self.prefix[i][j]

            self.prefix.append(total[:])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
