class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        next_greater = [-1] * len(nums)
        stack = []

        for idx in range(len(nums) * 2):
            num = nums[idx % len(nums)]

            while stack and nums[stack[-1]] < num:
                next_greater[stack.pop()] = num

            if idx < len(nums):
                stack.append(idx)

        return next_greater