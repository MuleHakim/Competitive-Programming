class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        while left + 1 < right:
            mid = (left + right) // 2
            result = 0
            for pile in piles:
                if pile > mid:
                    result += math.ceil(pile/mid)
                elif pile <= mid:
                    result += 1
                    
            if result > h:
                left = mid
            else:
                right = mid

        return right