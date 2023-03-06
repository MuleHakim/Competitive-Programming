class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        ans = []
        left = 0

        for right, char in enumerate(s):
            counter[char] -= 1

            while counter[char] < 0:
                counter[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
                
        return ans