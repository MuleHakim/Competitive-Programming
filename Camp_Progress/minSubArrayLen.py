class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = math.inf
        cur = 0
        left = 0

        for right in range(len(nums)):
            cur += nums[right]

            while cur >= target:
                count = min(count,right - left + 1)
                cur -= nums[left]
                left += 1

        if count == math.inf:
            return 0 
        return count
