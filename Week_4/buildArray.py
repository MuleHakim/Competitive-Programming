class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        length = len(nums)
        result = [0] * length

        for index in range(length):
            result[index] = nums[nums[index]]
            
        return result
