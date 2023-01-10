class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        integers = []
        if (num - 3) % 3 != 0:
            return integers
        integer1 = (num - 3) // 3

        integers = [integer1 + i for i in range(3)]

        return integers
