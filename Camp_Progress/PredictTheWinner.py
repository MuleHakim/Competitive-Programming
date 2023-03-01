class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(l,r):
            if l == r:
                return nums[l]
            return max(nums[l] - helper(l+1,r), nums[r] - helper(l,r-1))

        return helper(0,len(nums)-1) >= 0