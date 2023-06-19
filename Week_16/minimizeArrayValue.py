class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        for i in range(len(nums)):
            cur += nums[i]
            ans = max(ans, (cur + i) // (i + 1))
        return ans