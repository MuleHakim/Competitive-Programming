class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            min_height = min(height[left],height[right])
            cur_area = min_height * (right - left)
            maxArea = max(maxArea,cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
