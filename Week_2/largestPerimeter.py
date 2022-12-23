class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        length = len(nums)
        
        for pointer in range(length - 3, -1, -1):

            if nums[i] + nums[i + 1] > nums[ i + 2]:
                return nums[i] + nums[ i + 1] + nums[i + 2]

        return 0
