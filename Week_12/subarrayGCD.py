class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b:
                a,b = b, a % b
            return a
        count = 0

        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                curr = gcd(curr,nums[j])
                if(curr == k): 
                    count += 1 
        return count