class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lenRow = len(matrix)
        lenCol = len(matrix[0])
        low = 0
        high = lenRow * lenCol - 1

        while low <= high:
            mid = (low + high) // 2
            currRow = mid // lenCol
            currCol = mid % lenCol
            midElement = matrix[currRow][currCol]

            if midElement == target:
                return True
            elif midElement > target:
                high = mid -1
            else:
                low = mid + 1
                
        return False
