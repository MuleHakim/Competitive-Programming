class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        time_taken = 0

        while tickets[k] != 0:
            if i == len(tickets):
                i = 0
                continue
            if tickets[i] > 0:
                tickets[i] -= 1
                time_taken += 1
                
            i += 1

        return time_taken