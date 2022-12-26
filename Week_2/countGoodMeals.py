class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        listOfPower2 = []
        result = 0
        dictionary = defaultdict(int)

        for index in range(22):
            listOfPower2.append(pow(2,index))

        for eachDeli in deliciousness:
            
            for pow2 in listOfPower2:
                
                if pow2 - eachDeli in dictionary:
                    result += dictionary[pow2 - eachDeli]

            dictionary[eachDeli] += 1

        return result % (10**9 + 7)
