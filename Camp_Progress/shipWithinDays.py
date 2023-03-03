class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            day = 1
            wt_day = 0
            mid = (left + right) // 2
            for weight in weights:
                if wt_day + weight > mid:
                    day += 1
                    wt_day = 0
                wt_day += weight
                
            if day <= days:
                right = mid
            else:
                left = mid + 1
                
        return left