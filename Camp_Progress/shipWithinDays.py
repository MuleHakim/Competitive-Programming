class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            day = 1
            wt_day = 0
            capacity = (low + high) // 2
            for weight in weights:
                if wt_day + weight > capacity:
                    day += 1
                    wt_day = 0
                wt_day += weight
                
            if day <= days:
                high = capacity
            else:
                low = capacity + 1
        return low