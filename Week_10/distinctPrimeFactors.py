class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    res.add(d)
                    num //= d
                d += 1
            
            if num > 1:
                res.add(num)

        return len(res)