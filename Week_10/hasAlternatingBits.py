class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = n ^ (n >> 1)
        return num & (num + 1) == 0