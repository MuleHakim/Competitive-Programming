class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        result = -1
        minDistance = math.inf
        length = len(points)

        for pointer in range(length):

            if x == points[pointer][0] or y == points[pointer][1] :

                manhattanDistance = abs(points[pointer][0] - x) + \
                                    abs(points[pointer][1] - y)
                
                if manhattanDistance < minDistance:
                    minDistance = manhattanDistance
                    result = pointer

        return result
