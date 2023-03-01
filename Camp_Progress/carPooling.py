class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefixArr = [0] * 1001

        for trip in trips:
            passenger, pick, drop = trip
            prefixArr[pick] += passenger
            prefixArr[drop] -= passenger

        for i in range(1,len(prefixArr)):
            prefixArr[i] += prefixArr[i-1]

        if max(prefixArr) > capacity:
            return False

        return True