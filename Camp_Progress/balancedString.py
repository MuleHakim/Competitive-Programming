class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        n = len(s) // 4
        extras = {}

        for key in counter:
            if counter[key] > n:
                extras[key] = counter[key] - n

        if not extras: 
            return 0
            
        left = 0
        ans = len(s)
        for right in range(len(s)):
            if s[right] in extras:
                extras[s[right]] -= 1

            while max(extras.values()) == 0:
                ans = min(ans, right - left + 1)
                if s[left] in extras:
                    extras[s[left]] += 1
                left += 1

        return ans