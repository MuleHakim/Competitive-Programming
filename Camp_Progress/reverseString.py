class Solution:
    def reverseString(self, s: List[str]) -> None:
        # recursion

        # if len(s) < 2:
        #     return s
        # return self.reverseString(s[len(s)//2:]) + self.reverseString(s[:len(s)//2])

        # two pointers

        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1