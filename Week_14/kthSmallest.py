class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for r in range(n):
            for c in range(n):
                heapq.heappush(heap,-matrix[r][c])
        
        for _ in range(n*n-k):
            heapq.heappop(heap)

        return -heap[0]