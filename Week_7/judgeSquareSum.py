class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, floor(sqrt(c))
        if pow(right,2) == c: return True
        while left <= right:
            if pow(left,2) + pow(right,2) == c:
                return True
            if pow(left,2) + pow(right,2) < c:
                left += 1
            elif pow(left,2) + pow(right,2) > c:
                right -= 1
