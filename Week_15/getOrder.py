class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans, heap = [], []
        time = 0
        tasks.append([inf, inf])
        tasks = sorted([(enq, prc, idx) for idx, (enq, prc) in enumerate(tasks)])

        for enq, prc, i in tasks: 
            while heap and time < enq: 
                prc_time, idx, enq_time = heappop(heap)
                ans.append(idx)
                time = max(time, enq_time) + prc_time 

            heappush(heap, (prc, i, enq))

        return ans 