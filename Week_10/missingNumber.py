class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] != len(nums):
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                else:
                    break

        for i in range(len(nums)):
            if nums[i] != i:
                return i
                
        return len(nums)