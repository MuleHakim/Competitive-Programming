class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(int)
        cur_sum = 0
        ans = 0

        for num in nums:
            cur_sum += num
            
            if cur_sum == goal:
                ans += 1
            if cur_sum - goal in counter:
                ans += counter[cur_sum - goal]

            counter[cur_sum] += 1

        return ans