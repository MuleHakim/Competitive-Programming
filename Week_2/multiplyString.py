class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        eachSumList = []

        length1 = min(len(num1), len(num2))
        length2 = max(len(num1), len(num2))

        for index1 in range(length1 - 1, -1, -1):

            extra = 0 
            cur = ""
            for index2 in range(length2 - 1, -1, -1):

                if len(num1) < len(num2):
                    mult = int(num1[index1]) * int(num2[index2]) + extra
                else:
                    mult = int(num2[index1]) * int(num1[index2]) + extra 
                if index2 == 0:
                    cur += str(mult)[::-1]
                else:
                    cur += str(mult)[-1]
                    extra = (mult) // 10

            extraZero = "0" * (length1 - index1 - 1) 
            eachSumList.append(int(cur[::-1] + extraZero))

        result = str(sum(eachSumList))

        return result
