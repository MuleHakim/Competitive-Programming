class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        counter2 = defaultdict(int)
        left = 0

        for right in range(len(s2)):
            if right < len(s1) - 1:
                counter2[s2[right]] += 1

            else:
                counter2[s2[right]] += 1
                if counter2 == counter:
                    return True

                counter2[s2[left]] -= 1
                if counter2[s2[left]] == 0:
                    del counter2[s2[left]]  
                left += 1

        return False
