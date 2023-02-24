class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_val = 0
        for i in range(len(nums)):
            cur_val += nums[i]
            nums[i] = cur_val
        return nums
