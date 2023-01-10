class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        totalItems = len(matrix) * len(matrix[0])
        output = []

        r1 = 0
        c1 = 0
        r2 = len(matrix) - 1
        c2 = len(matrix[0]) - 1

        while len(output) < totalItems:

            indexCol = c1
            while indexCol <= c2 and len(output) < totalItems:
                output.append(matrix[r1][indexCol])
                indexCol += 1
            indexRow = r1 + 1
            while indexRow <= r2 - 1 and len(output) < totalItems:
                output.append(matrix[indexRow][c2])
                indexRow += 1
            indexCol = c2
            while indexCol >= c1 and len(output) < totalItems:
                output.append(matrix[r2][indexCol])
                indexCol -= 1
                
            indexRow = r2 - 1
            while indexRow >= r1 + 1 and len(output) < totalItems:
                output.append(matrix[indexRow][c1])
                indexRow -= 1

            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return output
    
