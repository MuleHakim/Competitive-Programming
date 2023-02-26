class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s)+1)
        ans = []

        for left, right, direction in shifts:

            if direction == 0:
                prefix[left] -= 1
                prefix[right + 1] += 1
            else:
                prefix[left] += 1
                prefix[right + 1] -= 1

        for idx, char in enumerate(s):
            shift = prefix[idx]
            ans.append(chr(((ord(char) - 97 + shift) % 26) + 97))
            prefix[idx + 1] += prefix[idx]

        return "".join(ans)