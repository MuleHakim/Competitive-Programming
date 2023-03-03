class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0, x
        while left <= right:
            mid = left +  (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                result = mid
                left = mid + 1
        return result