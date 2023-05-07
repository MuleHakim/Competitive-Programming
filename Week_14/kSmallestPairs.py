class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def inbound(i,j):
            return 0 <= i < len(nums1) and 0 <= j < len(nums2)

        heap = []
        heappush(heap,(nums1[0]+nums2[0], 0, 0))
        ans = [] 
        visited = set((0,0))
        while heap and len(ans) < k:
            pair_sum, u, v = heappop(heap)
            ans.append([nums1[u],nums2[v]])
            for i,j in ((1,0),(0,1)):
                if inbound(u+i,v+j) and (u+i,v+j) not in visited:
                    visited.add((u+i,v+j))
                    heappush(heap,(nums1[u+i]+nums2[v+j],u+i,v+j)) 
        return ans