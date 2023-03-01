class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(string):
            temp = ""
            for bit in string:
                if bit == "0":
                    temp += "1"
                else:
                    temp += "0"
            return temp
                
        def reverse(string):
            return string[::-1]
           
        def helper(n):
            if n == 1:
                return "0"
            temp = helper(n - 1)
            return temp + "1" + reverse(invert(temp))

        return helper(n)[k- 1]