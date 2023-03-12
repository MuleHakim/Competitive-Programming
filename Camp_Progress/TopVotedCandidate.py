class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

        counter = Counter()
        maxFreq = 1
        curValue = -1
        idx = 0
        for person in persons:
            counter[person] += 1
            if counter[person] == maxFreq:
                curValue = person
                persons[idx] = person
            elif counter[person] > maxFreq:
                curValue = person
                maxFreq += 1
                persons[idx] = person
            else:
                persons[idx] = curValue
            idx += 1

    def q(self, t: int) -> int:
        index = bisect.bisect_left(self.times,t)
        if t > self.times[-1]:
            return self.persons[-1]
        elif t == self.times[index]:
            return self.persons[index]
        return self.persons[index - 1]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)