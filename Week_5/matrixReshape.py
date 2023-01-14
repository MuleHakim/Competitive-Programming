class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        if m*n != c*r:
            return mat
            
        reshaped = [[0]*c for _ in range(r)]
        counter = 0
        for row in range(m):
            for col in range(n):
                reshaped[counter // c][counter % c] = mat[row][col]
                counter += 1
        
        return reshaped
