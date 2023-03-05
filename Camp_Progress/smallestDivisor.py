class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, 1000000
        smallest = 0
        while low < high:
            divisor = low + (high - low) // 2
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)
            if total <= threshold:
                smallest = divisor
                high = divisor
            else:
                low = divisor + 1
        return smallest