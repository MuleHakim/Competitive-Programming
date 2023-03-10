class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        cookies = sorted(cookies,reverse=True)
        children = [0 for _ in range(k)]

        def backtrack(index):
            if index >= len(cookies):
                return max(children)

            unfairness = float("inf")
            for idx in range(len(children)):
                children[idx] += cookies[index]
                if children[idx] < unfairness:
                    unfairness = min(unfairness, backtrack(index + 1))
                children[idx] -= cookies[index]

            return unfairness

        return backtrack(0)