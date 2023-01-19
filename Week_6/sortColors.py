class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        for idx in range(length - 1):

            while nums[idx] > nums[idx + 1] and idx >= 0:

                nums[idx],nums[idx + 1] = nums[idx + 1],nums[idx]
                idx -= 1

        return nums

