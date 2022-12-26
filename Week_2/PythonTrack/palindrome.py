class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        return False
