class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies = sorted(cookies,reverse=True)
        
        def backtrack(index, people):
            if index >= len(cookies):
                return max(people)

            fair = float("inf")
            for idx, person in enumerate(people):
                people[idx] += cookies[index]
                if people[idx] < fair:
                    fair = min(fair, backtrack(index + 1, people))
                people[idx] -= cookies[index]

            return fair

        return backtrack(0, [0 for _ in range(k)])