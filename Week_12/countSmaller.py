class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        indexed_nums = [(nums[key_index], key_index) for key_index in range(len(nums))]
        desc_nums, counts = self.mergeWithCount(indexed_nums, counts)
        return counts
	

    def mergeWithCount(self, nums, counts):
        if len(nums) <= 1:
            return nums, counts

        cur_stack = []
        mid = len(nums)//2
        left, counts = self.mergeWithCount(nums[:mid], counts)
        right, counts = self.mergeWithCount(nums[mid:], counts)
        
        
        while left and right:
            
            if left[0] > right[0]:
                counts[left[0][1]] += len(right) 
                cur_stack.append(left.pop(0))
            else:
                cur_stack.append(right.pop(0))
                
        if left:
            cur_stack.extend(left)
        else:
            cur_stack.extend(right)
            
        return cur_stack, counts