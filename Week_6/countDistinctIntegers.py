class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        dict_ = defaultdict(int)

        for num in nums:
            
            if len(str(num)) == 1:
                dict_[num] += 1
            else:
                dict_[num] += 1
                reverse = int(str(num)[::-1])
                dict_[reverse] += 1

        numOfDistinctInteger = len(dict_)

        return numOfDistinctInteger
