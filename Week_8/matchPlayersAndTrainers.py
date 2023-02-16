class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        maxNumMatch = 0
        players.sort()
        trainers.sort()
        for idx, trainer in enumerate(trainers):
            if players[maxNumMatch] <= trainers[idx]:
                maxNumMatch += 1
                if maxNumMatch == len(players):
                    return maxNumMatch
        return maxNumMatch
