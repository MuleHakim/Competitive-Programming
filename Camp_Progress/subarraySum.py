class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        my_dic = defaultdict(int)
        
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                count += 1
            if total-k in my_dic:
                count += my_dic[total-k]

            my_dic[total] += 1

        return count
