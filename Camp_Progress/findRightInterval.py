class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:   
        n = len(intervals) 
        intervals = sorted((interval[0], i, interval[1]) for i, interval in enumerate(intervals))
        ans = [0] * n
        
        for interval in intervals:
            start, index, end = interval
            r = bisect.bisect_left(intervals, (end,))

            if r < n:
                ans[index] = intervals[r][1]
            else:
                ans[index] = -1

        return ans