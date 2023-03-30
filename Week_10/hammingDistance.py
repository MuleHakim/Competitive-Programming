class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        for i in range(32):
            xi = yi = 0
            if x & (1 << i):
                xi = 1
            if y & (1 << i):
                yi = 1
            res += xi ^ yi
        return res