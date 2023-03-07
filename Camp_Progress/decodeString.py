# Stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ""

        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0

            elif char == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString

            elif char.isdigit():
                curNum = curNum*10 + int(char)
                
            else:
                curString += char

        return curString
# Recursion
class Solution:
    def decodeString(self, s: str) -> str:
        closedPos = {}
        stack = []
        for i, char in enumerate(s):
            if char == '[':
                stack.append(i)
            elif char == ']':
                closedPos[stack.pop()] = i

        def recur_Dfs(left, right):
            num = 0
            ans = []
            while left <= right:
                char = s[left]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '[':
                    ans.append(num * recur_Dfs(left + 1, closedPos[left] - 1))
                    num = 0
                    left = closedPos[left]
                else:
                    ans.append(char)
                left += 1
            return "".join(ans)

        return recur_Dfs(0, len(s) - 1)