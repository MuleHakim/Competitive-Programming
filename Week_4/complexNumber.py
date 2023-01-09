class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        index1 = num1.index("+")
        index2 = num1.index("i")

        index3 = num2.index("+")
        index4 = num2.index("i")

        realNum1 = int(num1[:index1])
        imagNum1 = int(num1[index1 + 1:index2])
        
        realNum2 = int(num2[:index3])
        imagNum2 = int(num2[index3 + 1: index4])

        multReal = str(realNum1 * realNum2 - imagNum1 * imagNum2)
        multImag = str(realNum1 * imagNum2 + imagNum1 * realNum2)
        finalMult = multReal + "+" + multImag + "i"

        return finalMult
