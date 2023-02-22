# Method 1
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums: return 1
        count = math.inf
        left = right = 0
        cur = nums[left]
        
        while left <= right and right < len(nums):
            if cur < target:
                right += 1
                if right < len(nums):
                    cur += nums[right]
            else:
                count = min(count, right - left + 1)
                cur -= nums[left]
                left += 1
                
        if count == math.inf:
            return 0 
        return count
        
# Method 2
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
