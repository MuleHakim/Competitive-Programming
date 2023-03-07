class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations)

        while low < high:
            mid = (low + high) // 2
            
            if citations[mid] >= len(citations) - mid:
                high = mid
            else:
                low = mid + 1

        return len(citations) - low