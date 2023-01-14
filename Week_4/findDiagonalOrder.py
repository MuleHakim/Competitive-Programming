class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])
        diagArray = []
        row = 0
        col = 0
        
        for idx in range(m*n):
            diagArray.append(mat[row][col])
            
            if (row + col) % 2 == 0:
                if col == m - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == n - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return diagArray
            
