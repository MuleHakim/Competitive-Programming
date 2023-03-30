class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num