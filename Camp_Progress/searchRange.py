class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        right = bisect_left(nums, target + 1)

        if left == right:
            return [-1, -1]
            
        return [left, right - 1]