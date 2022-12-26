class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:     

        length = len(matches)
        result = [[],[]]
        matchesDict = defaultdict(int)

        for index in range(length):
    
            matchesDict[matches[index][1]] += 1
            matchesDict[matches[index][0]] +=  0

        sorted_dictionary = sorted(matchesDict.items(), key=lambda x:x[0])
        sorted_dictionary = dict(sorted_dictionary)

        for key in sorted_dictionary.keys():
            
            if matchesDict[key]==0:
                result[0].append(key)

            elif matchesDict[key]==1:
                result[1].append(key)

        return result
