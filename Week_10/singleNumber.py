# O(32n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        shift = 1
        for i in range(32):
            count = 0
            for num in nums:
                if num & shift:
                    count += 1
            if count % 3 != 0:
                if i == 31: 
                    ans -= (2**31)
                else:
                    ans += shift
            shift *= 2
            
        return ans
# O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones