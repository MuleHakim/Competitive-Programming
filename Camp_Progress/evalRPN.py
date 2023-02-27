class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)

            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                if (a < 0 and b > 0) or ( a > 0 and b < 0):
                    stack.append(math.ceil(b / a))
                else:
                    stack.append(b // a)

            else:
                stack.append(int(token))

        return stack.pop()