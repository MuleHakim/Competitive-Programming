class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(s, l):
            if l == 0:
                return s
            return gcd(l, s % l)

        s, l = min(nums), max(nums)
        
        return gcd(s,l)