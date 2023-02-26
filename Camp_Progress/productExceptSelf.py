class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1 for _ in range(length)]

        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(length - 1, -1, -1):
            ans[i] = ans[i] * right_product
            right_product *= nums[i]

        return ans