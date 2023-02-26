class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for par in s:
            if par == '(':
                stack.append(0)
            else:
                cur_score = stack.pop()
                stack[-1] += max(2 * cur_score, 1)

        return stack[-1]