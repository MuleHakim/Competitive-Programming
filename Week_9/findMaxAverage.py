class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxSum = total

        for i in range(k, len(nums)):
            total -= nums[i - k]
            total += nums[i]
            maxSum = max(maxSum, total)

        return maxSum / k
