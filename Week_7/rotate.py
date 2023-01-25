class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length
        nums[:] = nums[length - k:] + nums[:length - k]
