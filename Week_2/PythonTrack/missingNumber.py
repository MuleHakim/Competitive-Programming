class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)
        sumOfNums = sum(nums)
        total = (length * (length + 1)) // 2
        
        return total - sumOfNums
