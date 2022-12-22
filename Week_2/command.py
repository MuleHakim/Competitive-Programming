class Solution:
    def interpret(self, command: str) -> str:

        result = ""
        length = len(command) - 1
        i = 0

        while i <= length:
            if command[i:i + 4] == "(al)":
                result += "al"
                i += 4
            elif command[i:i + 2] == "()":
                result += "o"
                i += 2
            else:
                result += command[i]
                i += 1

        return result
