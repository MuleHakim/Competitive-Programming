class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dic = defaultdict(int)
        max_len, left = 0, 0

        for right, char in enumerate(s):
            if char in my_dic:
                left = max(left, my_dic[char] + 1)
            max_len = max(max_len, right - left + 1)
            my_dic[char] = right

        return max_len
