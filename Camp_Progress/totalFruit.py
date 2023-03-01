class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = 0
        output = 0
        count = collections.defaultdict(int)

        for right, value in enumerate(fruits):
            count[value] += 1
            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
                
            output = max(output, right - left + 1)
            
        return output