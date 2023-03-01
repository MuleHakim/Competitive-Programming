class Solution:
    def reverseString(self, s: List[str]) -> None:
        # recursion
        left, right = 0, len(s) - 1

        def helper(l, r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            helper(l + 1, r - 1)
            
        helper(left, right)


        # two pointers
        # left, right = 0, len(s) - 1

        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1